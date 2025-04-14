document.getElementById('download-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = document.getElementById('url').value;
    const quality = document.getElementById('quality').value;
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = '⏳ Завантаження...';
  
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  
    const response = await fetch('/download/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({ url, quality })
    });
  
    if (response.ok) {
      const blob = await response.blob();
      const downloadUrl = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = downloadUrl;
      a.download = 'track.mp3';
      document.body.appendChild(a);
      a.click();
      a.remove();
      statusDiv.textContent = '✅ Завантажено';
    } else {
      statusDiv.textContent = '❌ Помилка при завантаженні';
    }
  });
  