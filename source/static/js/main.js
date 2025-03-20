document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar on mobile
    const sidebarToggle = document.getElementById('sidebar-toggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            const sidebar = document.querySelector('.sidebar');
            if (sidebar) {
                sidebar.classList.toggle('show-sidebar');
            }
        });
    }

    // Toggle analytics sidebar on mobile
    const analyticsSidebarToggle = document.getElementById('analytics-sidebar-toggle');
    if (analyticsSidebarToggle) {
        analyticsSidebarToggle.addEventListener('click', function() {
            const analyticsSidebar = document.querySelector('.analytics-sidebar');
            if (analyticsSidebar) {
                analyticsSidebar.classList.toggle('show-sidebar');
            }
        });
    }

    // Search form validation
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            const searchInput = document.getElementById('search-input');
            if (searchInput && searchInput.value.trim() === '') {
                event.preventDefault();
                searchInput.classList.add('is-invalid');
            }
        });
    }

    // Remove invalid class on input change
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            if (this.value.trim() !== '') {
                this.classList.remove('is-invalid');
            }
        });
    }

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Add semantic analysis functionality
    const analysisForm = document.getElementById('semantic-analysis-form');
    if (analysisForm) {
        analysisForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const analysisInput = document.getElementById('analysis-input');
            if (analysisInput && analysisInput.value.trim() !== '') {
                // Here you would normally send the data to the server
                // For now, we'll just show a message
                const resultContainer = document.getElementById('analysis-result');
                if (resultContainer) {
                    resultContainer.innerHTML = `
                        <div class="alert alert-info mt-3">
                            Аналіз виконується для тексту: "${analysisInput.value}"
                        </div>
                    `;
                }
            }
        });
    }
});
