function openModal() {
    document.getElementById("modal").classList.add("show");
}

function closeModal() {
    document.getElementById("modal").classList.remove("show");
}

window.addEventListener("click", function (event) {
    const modal = document.getElementById("modal");
    if (event.target === modal) {
        closeModal();
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
        closeModal();
    }
});

function filterIncidents() {
    const search = document.getElementById("searchInput").value.toLowerCase();
    const severity = document.getElementById("severityFilter").value;
    const rows = document.querySelectorAll(".incident-row");
    let visible = 0;

    rows.forEach(row => {
        const matchesSearch = row.dataset.search.includes(search);
        const matchesSeverity =
            severity === "ALL" || row.dataset.severity === severity;

        if (matchesSearch && matchesSeverity) {
            row.style.display = "";
            visible++;
        } else {
            row.style.display = "none";
        }
    });

    const noResults = document.getElementById("noResults");
    if (noResults) {
        noResults.style.display = visible === 0 ? "block" : "none";
    }
}
