const copyLinks = document.querySelectorAll('.btn');

copyLinks.forEach(elem => {
    elem.onclick = () => {
        const navText = elem.parentElement.childNodes[0].href;
        console.log(navText);
        navigator.clipboard.writeText(navText);
        elem.textContent = "Link Copied";
        
        setTimeout(() => {
            elem.textContent = "Copy Link";
        }, 5000);

        return;
    }
})
