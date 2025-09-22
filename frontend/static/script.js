document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-button');
    const chatMessages = document.getElementById('chat-messages');

    sendButton.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    async function sendMessage() {
        const userMessage = chatInput.value.trim();
        if (userMessage === '') {
            return;
        }

        appendMessage(userMessage, 'user-message');
        chatInput.value = '';

        try {
            // API call to the backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: userMessage })
            });

            const data = await response.json();
            
            if (response.ok) {
                appendMessage(data.response, 'chatbot-message');
            } else {
                appendMessage("Error: Could not get a response from the AI.", 'chatbot-message');
            }
        } catch (error) {
            console.error('Network Error:', error);
            appendMessage("I'm sorry, I'm having trouble connecting. Please try again.", 'chatbot-message');
        }
    }

    function appendMessage(text, senderClass) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', senderClass);
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});