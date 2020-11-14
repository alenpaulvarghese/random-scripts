# pastes.go

A handy CLI tool build using go to make quick and easy pastes.

-------

### Supported Service :-
- [dogbin](https://del.dog/)
- [nekobin](https://nekobin.com/)
- [hastbin](https://hastebin.com/)
- [github-gist](https://gist.github.com/)
------

## Available flags :-
        +-----------------------------+
	|  -f : read from a file      |
     	|  -n : use nekobin service   |
	|  -d : use dogbin service    |
        +-----------------------------+
        +-------------------------------------+
        | -g : use github-gist service        |
        | -D : description for gist           |
        | -p : publish created gist to public |
        +-------------------------------------+
<font color=yellow>INFO:</font> This binary package does not follow GNU parsing rules.

> ### Read from file -->
```
gist     : ./pastes -g -D "Hey this is my description" -f filename.txt
dogbin   : ./pastes -d -f filename.txt or ./pastes -f filename.txt
nekobin  : ./pastes -n -f filename.txt
hastebin : ./pastes -h -f filename.txt
```

> ### For singleline -->
```
gist     : ./pastes -g -p  -D "hey checkout this link" https://example.com
dogbin   : ./pastes https://example.com or ./pastes -d https://example.com
nekobin  : ./pastes -n Hey this is a test !
hastebin : ./pastes -d Hey this is a test !
```
> ### For multiline -->
```
gist     : ./pastes -g -p -D "Found a fix"
dobin    : ./pastes -d or ./pastes
nekobin  : ./pastes -n
hastebin : ./pastes -h
paste the content in nano editor and save the file without renaming.
```
-----
<font color="#DF2929">WARNING</font>  : make sure file flag `-f` or single line texts should'nt be placed before other flags.<br>
### Build commands : 
> building without api keys :
```bash
    go run -ldflags="-w" pastes.go
```
> building with only github API
```bash
    go build -ldflags="-X main.gistAPI=yourapikey -w" pastes.go
```
> building with only dogbin API
```bash
    go build -ldflags="-X main.dogbinAPI=yourapikey -w" pastes.go
```
> building with both github and dogbin API
```bash
    go build -ldflags="-X main.dogbinAPI=yourapikey -X main.gistAPI=yourapikey -w" pastes.go
```

