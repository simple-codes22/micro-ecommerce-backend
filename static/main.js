const copyLinks = document.querySelectorAll('.btn');

copyLinks.forEach(elem => {
    elem.onclick = () => {
        const navText = elem.parentElement.childNodes[0].href;
        console.log(navText);
        navigator.clipboard.writeText(navText);
        elem.textContent = "Link Copied";
        console.log("Text content changed");
        
        setTimeout(() => {
            elem.textContent = "Copy Link";
            console.log("Text content returned");
        }, 5000);

        return;
    }
})
