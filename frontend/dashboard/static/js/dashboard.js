const API_URL = "http://127.0.0.1:8000/api/dashboard/";

async function loadDashboard() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to fetch dashboard data");
        }

        const data = await response.json();

        console.log(data);

        // Cards
        document.getElementById("active-users").textContent = data.total_books;
        document.getElementById("books-out").textContent = data.issued_books;
        document.getElementById("acquisitions").textContent = data.total_copies;
        document.getElementById("total-fines").textContent = data.available_copies;

        // Other information
        document.getElementById("peak-report-time").textContent =
    data.peak_reporting;


document.getElementById("server-uptime").textContent =
    data.server_uptime;

        document.getElementById("featured-book-title").textContent = "Library Collection";
        document.getElementById("featured-book-author").textContent =
            data.total_authors + " Authors";
        document.getElementById("featured-book-progress").textContent =
            data.available_copies + " Copies Available";

        // Top Genres
        const genreContainer = document.getElementById("genre-container");

        genreContainer.innerHTML = `
            <div class="genre-item">
                <span class="rank">1</span>
                <div class="genre-info">
                    <h4>Total Categories</h4>
                    <small>${data.total_categories}</small>
                </div>
            </div>

            <div class="genre-item">
                <span class="rank">2</span>
                <div class="genre-info">
                    <h4>Total Authors</h4>
                    <small>${data.total_authors}</small>
                </div>
            </div>

            <div class="genre-item">
                <span class="rank">3</span>
                <div class="genre-info">
                    <h4>Total Publishers</h4>
                    <small>${data.total_publishers}</small>
                </div>
            </div>
        `;

        // Recent Inventory
        const inventoryTable = document.getElementById("inventory-table");

        inventoryTable.innerHTML = `
            <tr>
                <td>Books</td>
                <td>${data.total_books}</td>
                <td>System</td>
            </tr>

            <tr>
                <td>Issued</td>
                <td>${data.issued_books}</td>
                <td>System</td>
            </tr>

            <tr>
                <td>Available</td>
                <td>${data.available_copies}</td>
                <td>System</td>
            </tr>
        `;

    } catch (error) {
        console.error(error);
    }
}

loadDashboard();
document.getElementById("export-report").addEventListener("click", function(){

    let report = `
LIBRARY SYSTEM ANALYTICS REPORT

Total Books: ${document.getElementById("active-users").textContent}

Books Issued: ${document.getElementById("books-out").textContent}

Total Copies: ${document.getElementById("acquisitions").textContent}

Available Copies: ${document.getElementById("total-fines").textContent}

Generated Date: ${new Date().toLocaleDateString()}
`;

    let blob = new Blob([report], {
        type:"text/plain"
    });

    let link = document.createElement("a");

    link.href = URL.createObjectURL(blob);

    link.download = "Library_Report.txt";

    link.click();

});