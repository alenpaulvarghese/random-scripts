window.open(URL.createObjectURL(
    new Blob(
        [
            Array.from(
                document.getElementsByClassName("list-group-item list-group-item-action"))
                .map(x => x.getElementsByTagName('a')[1]?.href)
                .join("\n")
                .trim("\n")
        ], {
        type: "text/plain"
    })))