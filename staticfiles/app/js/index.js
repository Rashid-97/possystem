function qr_scanner() {
    const scanner = new Html5QrcodeScanner('reader', {
            // Scanner will be initialized in DOM inside element with id of 'reader'
            qrbox: {
                width: 250,
                height: 250,
            },  // Sets dimensions of scanning box (set relative to reader element width)
            fps: 20, // Frames per second to attempt a scan
        });


        scanner.render(success, error);
        // Starts scanner

        function success(result) {
            $("#result").html(result)
            scanner.clear();
            // Clears scanning instance
        }

        function error(err) {
            console.error(err);
            // Prints any errors to the console
        }
}