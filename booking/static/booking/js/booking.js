document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function() {
        const startTimeInput = document.getElementById('id_start_time');
        if (startTimeInput) {
            startTimeInput.addEventListener('change', function () {
                const selectedTime = this.value;
                const [hours, minutes] = selectedTime.split(':').map(Number);

                if (hours < 9 || hours >= 20) {
                    alert('Please select a time between 09:00 and 20:00');
                    this.value = '';
                }
            });
        }
    }, 100);
});