// script.js

// Get references to elements
const chatbotBtn = document.getElementById("chatbotBtn");
const chatbotPopup = document.getElementById("chatbotPopup");
const closeBtn = document.getElementById("closeBtn");
const sendMessageBtn = document.getElementById("sendMessageBtn");
const userInput = document.getElementById("userInput");
const chatbotBody = document.getElementById("chatbotBody");

// Open the chatbot popup when the button is clicked
chatbotBtn.addEventListener("click", () => {
    chatbotPopup.style.display = "block";
    userInput.focus();
});

// Close the chatbot popup when the close button is clicked
closeBtn.addEventListener("click", () => {
    chatbotPopup.style.display = "none";
});

// Handle sending the message
sendMessageBtn.addEventListener("click", () => {
    const userMessage = userInput.value.trim();

    if (userMessage) {
        // Display the user's message
        const userMessageElement = document.createElement("div");
        userMessageElement.classList.add("chatbot-message");
        userMessageElement.innerHTML = `<p>${userMessage}</p>`;
        chatbotBody.appendChild(userMessageElement);

        // Simulate the chatbot's response (Replace with actual chatbot logic)
        const chatbotResponseElement = document.createElement("div");
        chatbotResponseElement.classList.add("chatbot-message");
        chatbotResponseElement.innerHTML = `<p>Thank you for your message! We will get back to you shortly.</p>`;
        chatbotBody.appendChild(chatbotResponseElement);

        // Clear the input field
        userInput.value = "";
        chatbotBody.scrollTop = chatbotBody.scrollHeight;
    }
});

// Optionally, close the popup when the user presses the 'Escape' key
window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        chatbotPopup.style.display = "none";
    }
});
