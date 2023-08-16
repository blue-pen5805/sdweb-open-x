onUiLoaded(() => {
    gradioApp().querySelectorAll("#open_x").forEach((btn) => {
        btn.addEventListener("click", () => {
            window.open("https://twitter.com/share?&text=&hashtags=AI%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88")
        })
    })
})
