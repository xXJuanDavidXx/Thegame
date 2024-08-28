$(function() {

    // Obteniendo la URL del proyecto para la comunicación sockets
    var url = 'ws://' + window.location.host + '/ws/room/' + roomId + '/';
    console.log(url);

    // Creando comunicación WebSocket
    var chatSocket = new WebSocket(url);

    chatSocket.onopen = function(e) {
        console.log("WEBSOCKET OPEN");
    };

    chatSocket.onclose = function(e) {
        console.log("Cerrado");
    };

    // Aquí vamos a recibir la data que definimos en el consumers
    chatSocket.onmessage = function(data) {
        const datamsj = JSON.parse(data.data);
        var msj = datamsj.message;
        var username = datamsj.username;
        var datetime = datamsj.datetime;

        // Ahora vamos a imprimir los mensajes del otro usuario
        // Usando una estructura similar al envío del mensaje
        document.querySelector('#boxMessage').innerHTML +=
        `
        <div class="alert alert-success" role="alert">
            ${msj}
            <div>
                <small class="fst-italic fw-bold"> ${username} </small>
                <small class="float-end">${datetime}</small>
            </div>
        </div>
        `;
    };

    // Configurando el evento de enviar la información ya sea por click o presionando la tecla enter
    document.querySelector('#btnMessage').addEventListener('click', sendMessage);

    document.querySelector('#inputMessage').addEventListener('keypress', function(e) {
        if (e.keyCode == 13) {
            sendMessage();
        }
    });

    // Configurando la función que envía el mensaje y limpia el input cada que se envía
    function sendMessage() {
        var message = document.querySelector('#inputMessage');

        // Creando el envío del mensaje
        if (message.value.trim() !== '') {
            loadMessageHTML(message.value.trim());
            chatSocket.send(JSON.stringify({
                message: message.value.trim(),
            }));

            message.value = '';
        }
    }

    // Cómo se muestra el mensaje que envió el usuario
    function loadMessageHTML(m) {
	const dateObject = new Date()
	const año = dateObject.getUTCFullYear()
	const mes = dateObject.getMonth() + 1
	const dia = dateObject.getDay()
	const hora = dateObject.getHours()
	const minutos = dateObject.getMinutes()
	const segundos = dateObject.getSeconds()

	const formatofecha = `${año}-${mes}-${dia} ${hora}:${minutos}:${segundos}`


        document.querySelector('#boxMessage').innerHTML +=
        `
        <div class="alert alert-primary" role="alert">
            ${m}
            <div>
                <small class="fst-italic fw-bold"> ${usuario} </small>
                <small class="float-end">${formatofecha}</small>
            </div>
        </div>
        `;
    }

});

