<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panel de control</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 min-h-screen py-10 px-4">
  <div class="max-w-5xl mx-auto">
    <h1 class="text-3xl font-bold text-blue-700 text-center mb-4">Panel de control</h1>
    <p class="text-center text-gray-600 mb-10">Aquí puedes ver y gestionar los archivos XML.</p>

    <?php
    function parseDirectory($baseDir)
    {
      $items = scandir($baseDir);
      foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
          continue;
        }

        $fullPath = $baseDir . '/' . $item;

        if (is_dir($fullPath)) {
          echo "<div class='bg-white shadow rounded-lg mb-6 p-4'>";
          echo "<h2 class='text-xl font-semibold text-blue-600 mb-3'>📁 $item</h2>";
          echo "<ul class='divide-y divide-gray-200'>";
          parseDirectory($fullPath); // recursivo
          echo "</ul></div>";
        } elseif (pathinfo($fullPath, PATHINFO_EXTENSION) === 'xml') {
          echo "<li class='flex items-center justify-between py-2'>
                  <span class='text-gray-700'>$item</span>
                  <button onclick=\"viewContent('$fullPath')\" class='bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium px-3 py-1 rounded'>
                    Ver
                  </button>
                </li>";
        }
      }
    }

    $baseDir = 'xml';
    if (!is_dir($baseDir)) {
      echo "<p class='text-center text-red-600 font-semibold'>❌ El directorio XML no existe.</p>";
      exit;
    }

    echo "<ul class='space-y-4'>";
    parseDirectory($baseDir);
    echo "</ul>";
    ?>

    <!-- Modal -->
    <div id="contentModal" class="fixed inset-0 hidden bg-black bg-opacity-50 z-50 flex items-center justify-center">
      <div class="bg-white max-w-3xl w-full mx-4 rounded-lg shadow-lg p-6 overflow-auto max-h-[80vh] relative">
        <button onclick="closeModal()" class="absolute top-3 right-3 bg-red-600 hover:bg-red-700 text-white px-3 py-1 rounded text-sm">Cerrar</button>
        <h2 class="text-lg font-bold mb-4 text-gray-800">📄 Contenido del archivo</h2>
        <pre id="contentViewer" class="bg-gray-100 p-4 rounded border text-sm text-gray-800 overflow-auto whitespace-pre-wrap"></pre>
      </div>
    </div>

  </div>

  <script>
    function viewContent(filePath) {
      fetch(filePath)
        .then(response => {
          if (!response.ok) throw new Error('Failed to fetch file content.');
          return response.text();
        })
        .then(content => {
          const viewer = document.getElementById('contentViewer');
          viewer.textContent = content;
          const modal = document.getElementById('contentModal');
          modal.style.display = 'flex';
        })
        .catch(error => {
          alert('Error loading file content: ' + error.message);
        });
    }

    function closeModal() {
      const modal = document.getElementById('contentModal');
      modal.style.display = 'none';
    }
  </script>
</body>

</html>