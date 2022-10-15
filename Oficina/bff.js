function blink_x() {
    let request = new XMLHttpRequest()
    request.open("POST", "http://localhost:8000/arduino/blink_x", true)
    //request.setRequestHeader("Content-type", "application/json")
    //body={"vezes": document.getElementById("vezes").value}
    request.send(document.getElementById("vezes").value)
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