async function generateTutorial() {
    const components = document.querySelector('#components').value;
    const output = document.querySelector('#output');
    const imgElement = document.getElementById('myImage');
    const loadingElement = document.getElementById('loading');
    const loadingDots = document.getElementById('loading-dots');

    output.textContent = 'Generating an image for you...';
    loadingElement.style.display = 'block'; 
    imgElement.style.display = 'none'; 

    let dotCount = 0;
    const interval = setInterval(() => {
        dotCount = (dotCount + 1) % 4; 
        loadingDots.textContent = '.'.repeat(dotCount);
    }, 500);

    const response = await fetch('/generate', {
        method: 'POST',
        body: new FormData(document.querySelector('#tutorial-form'))
    });
    
    const imageUrl = await response.text();
    imgElement.src = imageUrl;
    clearInterval(interval);
    loadingElement.style.display = 'none'; 
    imgElement.style.display = 'block'; 
    output.textContent = 'Image generated!';
}

function copyToClipboard() {
    const imgElement = document.getElementById('myImage');
    const imageUrl = imgElement.src;
    const textarea = document.createElement('textarea');
    textarea.value = imageUrl;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Copied to clipboard');
}
