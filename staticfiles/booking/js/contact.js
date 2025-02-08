(function(){
    emailjs.init('s1WFcW4TpyIQx8nLn');
})();


document.getElementById('contact-form').addEventListener('submit', function(event){
    event.preventDefault();
    
    // Get form data
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value
    };

    console.log(formData)

    emailjs.send('service_9h2qju5', 'template_wzq4t5r', formData)
        .then(function(response) {
            alert('Thank you for contacting us! We will get back to you soon.');
            document.getElementById('contact-form').reset();
        }, function(error) {
            alert('Oops! Something went wrong. Please try again.');
            console.log(error)
        });

})