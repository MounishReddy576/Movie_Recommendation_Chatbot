function send() {
	var input = document.querySelector("input").value;
	if (input) {
		addUserMessage(input);
		getBotMessage(input);
		document.querySelector("input").value = "";
	}
}

function addUserMessage(message) {
	var messages = document.querySelector(".messages");
	var userMessage = document.createElement("div");
	userMessage.className = "user-message";
	userMessage.innerHTML = "<p>" + message + "</p>";
	messages.appendChild(userMessage);
	messages.scrollTop = messages.scrollHeight;
}

function getBotMessage(message) {
	fetch("/recommendation?message=" + message)
		.then(response => response.json())
		.then(data => {
			var messages = document.querySelector(".messages");
			var botMessage = document.createElement("div");
			botMessage.className = "bot-message";
			botMessage.innerHTML = "<p>" + data.message + "</p>";
			messages.appendChild(botMessage);
			messages.scrollTop = messages.scrollHeight;
		});
}
