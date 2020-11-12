/*
(c) AlenPaulVarghese

__version__: 2.0

Available flags :-
		-f : read from a file
		-n : use nekobin service
		-d : use dogbin service
INFO: to use dogbin api key while building use the following bulid command
	command: go build -ldflags="-X main.dogbinAPI=yourapikey" pastes.go
--------------------------------------------------------------------------
Read from file -->
dogbin   : ./pastes -d -f filename.txt or ./pastes -f filename.txt
nekobin  : ./pastes -n -f filename.txt
hastebin : ./pastes -h -f filename.txt
WARNING  : make sure file flag `-f` should'nt be placed before other flags.
--------------------------------------------------------------------------
To get short links -->
dogbin   : ./pastes https://example.com or ./pastes -d https://example.com
nekobin  : ./pastes -n https://example.com
hastebin : ./pastes -d https://example.com
--------------------------------------------------------------------------
For multiline -->
dobin    : ./pastes -d or ./pastes
nekobin  : ./pastes -n
hastebin : ./pastes -h
paste the content in nano editor and save the file without renaming.
--------------------------------------------------------------------------
*/
package main

import (
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
	hastebinURL = "https://hastebin.com/"
	nekobinURL  = "https://nekobin.com/"
	dogbinURL   = "https://del.dog/"
)

var (
	file      = flag.String("f", "", "file path to read from")
	haste     = flag.Bool("h", false, "use hastebin")
	neko      = flag.Bool("n", false, "use nekobin")
	dog       = flag.Bool("d", false, "use dogbin")
	client    = &http.Client{}
	link      = ""
	dogbinAPI = ""
)

func main() {
	flag.Parse()
	var id string
	switch true {
	case *file != "" && *neko:
		nekobin(filereader(*file), &id)
	case *file != "" && *haste, (*file != ""):
		paster(filereader(*file), &id)
	default:
		var message string
		if len(flag.Args()) == 0 {
			message = nano()
		} else {
			message = strings.Join(flag.Args(), " ")
		}
		if *neko {
			nekobin(message, &id)
		} else {
			paster(message, &id)
		}
	}
	fmt.Printf("Your Link --> %s\nRaw Link  --> %s\n", link+id, link+"raw/"+id)
}

func nekobin(message string, id *string) {
	link = nekobinURL
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
	*id = (fmt.Sprint(m["result"].(map[string]interface{})["key"]))
}

func paster(message string, id *string) {
	if *haste {
		link = hastebinURL
	} else {
		link = dogbinURL
	}
	status := strings.NewReader(message)
	request, _ := http.NewRequest("POST", link+"documents", status)
	request.Header.Set("Content-Type", "text/plain; charset=UTF-8")
	if dogbinAPI != "" && !*haste {
		request.Header.Set("X-Api-Key", dogbinAPI)
	}
	resp, err := client.Do(request)
	if err != nil {
		log.Fatalf("Failed to connect to %s server", link)
	}
	defer resp.Body.Close()
	var m map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&m)
	*id = fmt.Sprint(m["key"])
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
