// Test file for the calendar component

describe('Calendar Component Tests', () => {
    let calendar, currentMonth, prevMonthBtn, nextMonthBtn;

    beforeEach(() => {
        document.body.innerHTML = `
            <div class="container">
                <button id="prevMonth">&lt; Prev</button>
                <h3 id="currentMonth"></h3>
                <button id="nextMonth">Next &gt;</button>
                <div id="calendar"></div>
            </div>
        `;

        calendar = document.getElementById('calendar');
        currentMonth = document.getElementById('currentMonth');
        prevMonthBtn = document.getElementById('prevMonth');
        nextMonthBtn = document.getElementById('nextMonth');

        date = new Date();

        renderCalendar();
    });

    afterEach(() => {
        document.body.innerHTML = '';
    });

    test('should render the correct number of days for the current month', () => {
        const daysInMonth = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
        const dayElements = calendar.querySelectorAll('.day:not(.header)');
        expect(dayElements.length).toBe(daysInMonth + date.getDay());
    });

    test('should update month title on navigation', () => {
        const initialMonth = date.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });

        prevMonthBtn.click();
        const prevMonthTitle = new Date(date.setMonth(date.getMonth() - 1)).toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
        expect(currentMonth.textContent).toBe(prevMonthTitle);

        nextMonthBtn.click();
        const nextMonthTitle = new Date(date.setMonth(date.getMonth() + 1)).toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
        expect(currentMonth.textContent).toBe(nextMonthTitle);
    });

    test('should log correct date on day click', () => {
        console.log = jest.fn();
        const dayElement = calendar.querySelector('.day:not(.header):not(:empty)');
        const selectedDate = dayElement.dataset.date;

        dayElement.click();

        expect(console.log).toHaveBeenCalledWith(`You clicked on: ${selectedDate}`);
    });

    test('should display alert with selected date on day click', () => {
        window.alert = jest.fn();
        const dayElement = calendar.querySelector('.day:not(.header):not(:empty)');
        const selectedDate = dayElement.dataset.date;

        dayElement.click();

        expect(window.alert).toHaveBeenCalledWith(`Selected Date: ${selectedDate}`);
    });
});
