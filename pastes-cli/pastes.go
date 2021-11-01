/*
(c) AlenPaulVarghese
__version__: 2.5 */
package main

import (
	"bytes"
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"strings"
)

const (
	gistURL     = "https://api.github.com"
	hastebinURL = "https://hastebin.com/"
	nekobinURL  = "https://nekobin.com/"
	dogbinURL   = "https://del.dog/"
)

var (
	file      = flag.String("f", "", "input file")
	desc      = flag.String("D", "", "description for github gist")
	public    = flag.Bool("p", false, "publish created gist to public")
	gist      = flag.Bool("g", false, "use github-gist service")
	haste     = flag.Bool("h", false, "use hastebin service")
	neko      = flag.Bool("n", false, "use nekobin service")
	dog       = flag.Bool("d", false, "use dogbin service")
	client    = &http.Client{}
	dogbinAPI = ""
	gistAPI   = ""
)

type pasteResponse struct {
	Primary string
	Raw     string
}

func main() {
	flag.Parse()
	var response pasteResponse
	switch true {
	case *file != "" && *neko:
		nekobin(filereader(*file), &response)
	case *file != "" && *gist:
		gisthub(filereader(*file), &response)
	case *file != "" && *haste, (*file != ""):
		paster(filereader(*file), &response)
	default:
		var message string
		if len(flag.Args()) == 0 {
			message = nano()
		} else {
			message = strings.Join(flag.Args(), " ")
		}
		if *neko {
			nekobin(message, &response)
		} else if *gist {
			*file = "paste.txt"
			gisthub(message, &response)
		} else if *haste || *dog {
			paster(message, &response)
		}
	}
	fmt.Printf("Your Link --> %s\nRaw Link  --> %s\n", response.Primary, response.Raw)
}

func nekobin(message string, p *pasteResponse) {
	payload := strings.NewReader(url.Values{"content": {message}}.Encode())
	request, _ := http.NewRequest(http.MethodPost, nekobinURL+"api/documents", payload)
	request.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	resp, err := client.Do(request)
	if err != nil {
		log.Fatalf("Failed to connect to %s server", nekobinURL)
	}
	defer resp.Body.Close()
	var m map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&m)
	p.Primary = nekobinURL + fmt.Sprint(m["result"].(map[string]interface{})["key"])
	p.Raw = nekobinURL + "raw/" + fmt.Sprint(m["result"].(map[string]interface{})["key"])
}

func paster(message string, p *pasteResponse) {
	var endpoint string
	if *haste {
		endpoint = hastebinURL
	} else if *dog {
		endpoint = dogbinURL
	}
	status := strings.NewReader(message)
	request, _ := http.NewRequest("POST", endpoint+"documents", status)
	request.Header.Set("Content-Type", "text/plain; charset=UTF-8")
	if dogbinAPI != "" && !*haste {
		request.Header.Set("X-Api-Key", dogbinAPI)
	}
	resp, err := client.Do(request)
	if err != nil {
		log.Fatalf("Failed to connect to %s server", endpoint)
	}
	defer resp.Body.Close()
	var m map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&m)
	p.Primary = endpoint + fmt.Sprint(m["key"])
	p.Raw = endpoint + "raw/" + fmt.Sprint(m["key"])
}

func gisthub(message string, p *pasteResponse) {
	if gistAPI == "" {
		log.Fatal("cannot create gists without github personal access token")
	}
	body, _ := json.Marshal(map[string]interface{}{
		"files":       map[string]interface{}{*file: map[string]interface{}{"content": message}},
		"public":      *public,
		"description": *desc,
	})
	request, _ := http.NewRequest(http.MethodPost, gistURL+"/gists", bytes.NewBuffer(body))
	request.Header.Add("Accept", "application/vnd.github.v3+json")
	request.Header.Add("Authorization", "token "+gistAPI)
	resp, err := client.Do(request)
	if err != nil {
		fmt.Println(err)
		log.Fatalf("Failed to connect to %s server", gistURL)
	}
	defer resp.Body.Close()
	var m map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&m)
	p.Primary = fmt.Sprint(m["html_url"])
	p.Raw = fmt.Sprint(m["files"].(map[string]interface{})[*file].(map[string]interface{})["raw_url"])
}

func filereader(filename string) string {
	file, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(file)
}

func nano() string {
	filename := "PasteYouContentHere"
	cmd := exec.Command("nano", filename)
	cmd.Stdin, cmd.Stdout, cmd.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := cmd.Start(); err != nil {
		log.Fatal("Please install nano !")
	}
	cmd.Wait()
	if _, err := os.Stat(filename); err != nil {
		log.Fatal(err)
	}
	defer os.Remove(filename)
	return filereader(filename)
}
