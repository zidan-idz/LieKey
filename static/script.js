// Menampilkan input sesuai algoritma
function toggleInput() {
    const algo = document.getElementById("algo").value;
    const shiftDiv = document.getElementById("shiftDiv");
    const keyDiv = document.getElementById("keyDiv");

    if (algo === "caesar") {
        shiftDiv.style.display = "block";
        keyDiv.style.display = "none";
    } else {
        shiftDiv.style.display = "none";
        keyDiv.style.display = "block";
    }
}

// Mengubah teks tombol berdasarkan mode
function updateButtonText() {
    const mode = document.getElementById("mode").value;
    const button = document.getElementById("executeButton");

    if (mode === "encrypt") {
        button.innerHTML = '<i class="bi bi-lock"></i> Enkripsi';
        button.classList.remove('btn-info');
        button.classList.add('btn-primary');
    } else {
        button.innerHTML = '<i class="bi bi-unlock"></i> Dekripsi';
        button.classList.remove('btn-primary');
        button.classList.add('btn-info');
    }
}

// Jalankan otomatis saat halaman dimuat
window.addEventListener("load", updateButtonText);
