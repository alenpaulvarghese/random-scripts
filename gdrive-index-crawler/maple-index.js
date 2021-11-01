window.open(
    URL.createObjectURL(
        new Blob(
            [
                $$("a.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--light.v-size--default")
                    .map(x => x.href)
                    .join("\n")
            ], {
            type: "text/plain"
        })))