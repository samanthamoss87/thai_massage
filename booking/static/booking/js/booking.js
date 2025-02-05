document.addEventListener('DOMContentLoaded', function () {
    const startTimeInput = document.getElementById('id_start_time');

    startTimeInput.addEventListener('change', function () {
        const selectedTime = this.value;
        const [hours, minutes] = selectedTime.split(':').map(Number);

        if (hours < 9 || hours >= 20) {
            alert('Please select a time between 09:00 and 20:00');
            this.value = '';
        }
    });
});



// Email.js functionality
document.getElementById('booking-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const formData = {
      to_email: '{{ request.user.email }}', // Customer's email (recipient)
      customer_name: '{{ request.user.username }}', // Customer's name
      treatment: this.treatment.value, // Selected treatment
      date: this.date.value, // Selected date
      start_time: this.start_time.value, // Selected start time
      duration: this.duration.value, // Selected duration
    };

    // Send the email using EmailJS
    emailjs.send('service_9h2qju5', 'template_wzq4t5r', formData)
      .then(function(response) {
        alert('Booking successful! Check your email for confirmation.');
        console.log('SUCCESS!', response.status, response.text);
        // Optionally, submit the form to the server after sending the email
        event.target.submit();
      }, function(error) {
        alert('Failed to send email. Please try again.');
        console.log('FAILED...', error);
      });
  });