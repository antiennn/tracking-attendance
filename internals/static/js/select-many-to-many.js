document.addEventListener("DOMContentLoaded", function() {
  const selects = document.querySelectorAll('select[data-role="choices"]');
  selects.forEach(select => {
    new Choices(select, {
      removeItemButton: true,
      placeholder: true,
      placeholderValue: "Find IP...",
      searchPlaceholderValue: "Search IP...",
      allowHTML: true,
    });
  });
});
