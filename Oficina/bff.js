function blink_x() {
    let request = new XMLHttpRequest()
    url = "http://localhost:8000/arduino/blink_x/"+document.getElementById("vezes").value
    request.open("POST", url, true)
    request.send()
    return request.responseText
}

function ler_led() {
    let request = new XMLHttpRequest()
    request.open("GET","http://localhost:8000/arduino/ler_led", false)
    request.send()
    return request.responseText
}

function ler_botao() {
    let request = new XMLHttpRequest()
    request.open("GET","http://localhost:8000/arduino/ler_botao", false)
    request.send()
    return request.responseText
}

function not_led() {
    let request = new XMLHttpRequest()
    request.open("GET","http://localhost:8000/arduino/not_led", false)
    request.send()
    return request.responseText
}
