spinList = ["static/images/spin1.png", "static/images/spin45.png", "static/images/spin90.png",
    "static/images/spin135.png", "static/images/spin180.png", "static/images/spin225.png",
"static/images/spin270.png", "static/images/spin315.png"]

$('#spinclick').click(function () {
    for (let i = 0; i < spinList.length; i++) {
    setInterval($('#spin').attr("src", spinList[i]), 3000)
}
})

$('#spinclick').click(function () {
    $('#spin').attr("src", "https://placekitten.com/640/360")
})




for (let i = 0; i < spinList.length; i++) {
    setInterval($('#spin').attr("src", spinList[i]), 3000)
}
