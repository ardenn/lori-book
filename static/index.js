const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        greeting: 'Hello, from Vue!',
        books: [],
        showForm: true,
        charges: []
    },
    methods: {
        addBook: function () {
            this.showForm = true;
            this.books.push({ borrow_date: Date(), return_date: Date() })
        },
        resetBooks: function () {
            this.books = []
            this.showForm = true;
            this.charges = []
        },
        getCharges: async function () {
            const response = await fetch("http://127.0.0.1:5000/charges", {
                method: "POST", headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.books)
            });
            this.charges = await response.json();
            this.showForm = false
        }
    }
})