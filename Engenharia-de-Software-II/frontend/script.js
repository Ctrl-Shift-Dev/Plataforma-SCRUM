// frontend/script.js

// Função para buscar FAQ do servidor
async function fetchFAQ(query = '') {
    const response = await fetch(query ? `/faq/search?query=${query}` : '/faq');
    const faqData = await response.json();
    displayFAQ(faqData);
}

// Função para exibir perguntas e respostas
function displayFAQ(faqData) {
    const faqContainer = document.getElementById('faq-container');
    faqContainer.innerHTML = '';

    faqData.forEach(item => {
        const faqItem = document.createElement('div');
        faqItem.classList.add('faq-item');

        const question = document.createElement('h3');
        question.innerText = `${item.category} - ${item.question}`;
        question.onclick = () => {
            answer.style.display = answer.style.display === 'none' ? 'block' : 'none';
        };

        const answer = document.createElement('p');
        answer.innerText = item.answer;

        faqItem.appendChild(question);
        faqItem.appendChild(answer);
        faqContainer.appendChild(faqItem);
    });
}

// Função para enviar o FAQ por email
async function sendFAQEmail() {
    try {
        const response = await fetch('/send-faq', { method: 'POST' });
        if (response.ok) {
            alert('FAQ enviado com sucesso para o email andreneves6663234@gmail.com!');
        } else {
            alert('Erro ao enviar o FAQ por email.');
        }
    } catch (error) {
        alert('Erro ao enviar o FAQ por email.');
    }
}

// Adiciona o evento de busca
document.getElementById('search').addEventListener('input', (e) => {
    const query = e.target.value.trim();
    fetchFAQ(query);
});

// Adiciona o evento de clique para enviar o email
document.getElementById('sendEmail').addEventListener('click', sendFAQEmail);

// Carrega o FAQ inicial
fetchFAQ();
