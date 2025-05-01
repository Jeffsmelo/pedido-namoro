import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Pedido Especial", layout="wide")

components.html(
    """
    <html>
    <head>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            margin-top: 100px;
            color: white;
            background-image: url('https://i.imgur.com/4NJlVnW.jpg'); /* Imagem de fundo com corações */
            background-size: cover;
            background-position: center;
            height: 100vh;
            overflow: hidden;
        }
        .overlay {
            background-color: rgba(0, 0, 0, 0.5);
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: -1;
        }
        .question {
            font-size: 40px;
            margin-bottom: 50px;
        }
        .btn {
            padding: 15px 40px;
            font-size: 24px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin: 20px;
        }
        .yes {
            background-color: #28a745;
            color: white;
        }
        .no {
            background-color: #dc3545;
            color: white;
            position: absolute;
        }
    </style>
    </head>
    <body>
        <div class="overlay"></div>
        <div class="question">💖 Quer ser minha pra sempre? 💖</div>
        <button class="btn yes" onclick="showFireworks()">Sim</button>
        <button id="noBtn" class="btn no" style="top: 60%; left: 60%;">Não</button>

        <canvas id="canvas" style="position: fixed; top: 0; left: 0; width:100%; height:100%; pointer-events: none;"></canvas>

        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
        <script>
            const btn = document.getElementById("noBtn");

            document.addEventListener("mousemove", function(e) {
                const x = e.clientX;
                const y = e.clientY;
                const rect = btn.getBoundingClientRect();
                const bx = rect.left + rect.width / 2;
                const by = rect.top + rect.height / 2;
                const distance = Math.hypot(x - bx, y - by);
                if (distance < 150) {
                    const newX = Math.random() * (window.innerWidth - rect.width);
                    const newY = Math.random() * (window.innerHeight - rect.height);
                    btn.style.left = `${newX}px`;
                    btn.style.top = `${newY}px`;
                }
            });

            function showFireworks() {
                document.body.innerHTML = '<h1 style="margin-top: 200px; font-size: 60px; color: white;">🎆 EBAAA! Eu te amo! ❤️</h1>';
                setInterval(() => {
                    confetti({
                        particleCount: 150,
                        spread: 70,
                        origin: { y: 0.6 }
                    });
                }, 800);
            }
        </script>
    </body>
    </html>
    """,
    height=800,
)
