# Available flags :-<br>
		-f : read from a file
		-n : use nekobin service
		-d : use dogbin service
INFO: to use dogbin api key while building use the following bulid command
	command: go build -ldflags="-X main.dogbinAPI=yourapikey" pastes.go

## Read from file -->
>dogbin &nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;```./pastes -d -f filename.txt or ./pastes -f filename.txt```<br>
>nekobin &nbsp;&nbsp;:&nbsp; ```./pastes -n -f filename.txt```<br>
>hastebin &nbsp;:&nbsp; ```./pastes -h -f filename.txt```<br>

# WARNING  : make sure file flag `-f` should'nt be placed before other flags.
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