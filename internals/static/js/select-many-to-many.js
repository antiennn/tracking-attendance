function copyToClipboard(text) {
    navigator.clipboard.writeText(window.location.origin + text).then(() => {
        toastr.success("Copied successful");
    });
}
