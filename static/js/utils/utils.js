// ========== FUNCIONES GLOBALES WALLET ==========
(function() {
    'use strict';
    
    window.showRedirectOverlay = function(message = 'Cargando...', url = 'menu.html') {
        const existingOverlay = document.getElementById('redirect-overlay');
        if (existingOverlay) existingOverlay.remove();
        
        const overlay = document.createElement('div');
        overlay.id = 'redirect-overlay';
        overlay.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.9); display: flex; align-items: center;
            justify-content: center; z-index: 9999; backdrop-filter: blur(8px);
        `;

        let countdown = 3; // Segundos de espera

        overlay.innerHTML = `
            <div style="
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white; padding: 3rem 2rem; border-radius: 24px;
                text-align: center; box-shadow: 0 25px 50px rgba(0,0,0,0.3);
                max-width: 400px; width: 90%; border: 1px solid rgba(255,255,255,0.2);
            ">
                <div style="
                    width: 80px; height: 80px; background: rgba(255,255,255,0.2);
                    border-radius: 50%; display: flex; align-items: center;
                    justify-content: center; margin: 0 auto 2rem;
                    font-size: 3rem; animation: pulse 1.5s infinite;
                ">
                    ✅
                </div>
                <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem;">${message}</h2>
                <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 1.5rem;">
                    Redirigiendo en <span id="countdown-global" style="font-weight: bold;">${countdown}</span> segundos...
                </p>
                <div style="
                    width: 100%; height: 6px; background: rgba(255,255,255,0.2);
                    border-radius: 10px; overflow: hidden; margin: 0 auto;
                ">
                    <div id="progress-bar-global" style="
                        height: 100%; background: #10b981; width: 0%;
                        transition: width 1s linear;
                    "></div>
                </div>
            </div>
        `;

        if (!document.getElementById('global-redirect-styles')) {
            const style = document.createElement('style');
            style.id = 'global-redirect-styles';
            style.textContent = `
                @keyframes pulse {
                    0% { transform: scale(1); opacity: 1; }
                    50% { transform: scale(1.1); opacity: 0.7; }
                    100% { transform: scale(1); opacity: 1; }
                }
            `;
            document.head.appendChild(style);
        }

        document.body.appendChild(overlay);

        // Lógica del contador y barra
        const totalTime = countdown;
        const interval = setInterval(() => {
            countdown--;
            
            // Actualizar texto
            const counterEl = document.getElementById('countdown-global');
            if (counterEl) counterEl.textContent = countdown;

            // Actualizar barra (proporcional)
            const progressEl = document.getElementById('progress-bar-global');
            if (progressEl) {
                const percentage = ((totalTime - countdown) / totalTime) * 100;
                progressEl.style.width = percentage + '%';
            }

            if (countdown <= 0) {
                clearInterval(interval);
                window.location.href = url;
            }
        }, 1000);
    };
})();