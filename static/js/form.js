/* 
   EscTrix Secure Contact Form — Formspree AJAX Handler
*/

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('secure-contact-form');
    const statusBox = document.getElementById('form-status-box');

    if (!form || !statusBox) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // UI Feedback - Processing
        const submitBtn = form.querySelector('.btn-form-submit');
        const originalText = submitBtn.textContent;
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'TRANSMITTING ENCRYPTED MESSAGE... <span class="spinner"></span>';
        
        statusBox.className = 'form-status';
        statusBox.style.display = 'none';

        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (response.ok) {
                // Success path
                statusBox.textContent = 'Your message has been securely transmitted. Our development team will review it and contact you shortly.';
                statusBox.className = 'form-status success';
                form.reset();
            } else {
                // Error path
                const result = await response.json();
                let errorMessage = 'Transmission error: ';
                if (result.errors) {
                    errorMessage += result.errors
                        .map(err => err.message)
                        .join(' | ');
                } else {
                    errorMessage += 'Validation failed. Please check your inputs.';
                }
                statusBox.textContent = errorMessage;
                statusBox.className = 'form-status error';
            }
        } catch (error) {
            statusBox.textContent = 'Transmission blocked or connection failed. Please attempt again or email directly.';
            statusBox.className = 'form-status error';
        } finally {
            // Restore button
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
            statusBox.style.display = 'block';
            
            // Auto scroll to status message
            statusBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    });
});
