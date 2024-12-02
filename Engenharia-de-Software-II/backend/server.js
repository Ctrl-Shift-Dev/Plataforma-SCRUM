const express = require('express');
const nodemailer = require('nodemailer');
const path = require('path');
const app = express();
const PORT = 3000;

app.use(express.json()); // Para lidar com JSON no corpo da requisição
app.use(express.static(path.join(__dirname, '../frontend')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

// Configuração do transporte de email com Nodemailer
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'anrdreteste@gmail.com',  // Substitua pelo seu email
        pass: '12312378'                // Sua senha de app ou senha do Gmail
    }
});

// Endpoint para receber as cores selecionadas e enviar o e-mail
app.post('/send-colors', (req, res) => {
    const { colors } = req.body;

    // Verifica se as cores estão presentes
    if (!colors || colors.length === 0) {
        return res.status(400).json({ message: 'Nenhuma cor selecionada.' });
    }

    // Construir o conteúdo do email com as cores
    let emailContent = `Cores selecionadas: ${colors.join(', ')}`;

    const mailOptions = {
        from: 'anrdreteste@gmail.com',  // Seu email de origem
        to: 'andreneves6663234@gmail.com',  // Email de destino
        subject: 'Cores Selecionadas',
        text: emailContent
    };

    // Enviar o email
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log('Erro ao enviar email:', error);
            return res.status(500).json({ message: 'Erro ao enviar o email.' });
        } else {
            console.log('Email enviado:', info.response);
            return res.status(200).json({ message: 'Email enviado com sucesso.' });
        }
    });
});

// Endpoint para enviar o FAQ
app.post('/send-faq', (req, res) => {
    const { faq } = req.body;

    // Construir o conteúdo do email com FAQ
    let emailContent = 'FAQ:\n\n';
    faq.forEach(item => {
        emailContent += `Pergunta: ${item.question}\nResposta: ${item.answer}\n\n`;
    });

    const mailOptions = {
        from: 'anrdreteste@gmail.com',  // Seu email de origem
        to: 'andreneves6663234@gmail.com',  // Email de destino
        subject: 'FAQ Enviado',
        text: emailContent
    };

    // Enviar o email
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log('Erro ao enviar email:', error);
            return res.status(500).json({ message: 'Erro ao enviar o email.' });
        } else {
            console.log('Email enviado:', info.response);
            return res.status(200).json({ message: 'Email enviado com sucesso.' });
        }
    });
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
