document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelector('#form').onsubmit = () => {
        
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert');

        // Callback function for when request compeltes
        request.onload = () => {
            //Extract json data from request
            const data = JSON.parse(request.responseText);
            console.log(data);
            //Update div result
            if(data.success){
                const contents = `1 Error is equal to ${data.code} in ${currency}.`
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = "Something went wrong.";
            }
            
            console.log(contents);
        };
        //Add data to send in request
        const fdata = new FormData();
        fdata.append('currency', currency);
        console.log(fdata);

        //Send request
        request.send(fdata);
        return false;
    };
});