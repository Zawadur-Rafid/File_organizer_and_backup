<!DOCTYPE html>
<html lang="en">
<head> 
</head>
<body>

<h1>File Organizer & Backup</h1>

<p>A <strong>Python-based utility</strong> to automatically organize files into categorized folders and create backups of important data. This tool helps maintain a clean and structured file system while keeping your files safe.</p>

<h2>Features</h2>
<ul>
    <li>Automatically organizes files by type (e.g., documents, images, videos, audio, archives)</li>
    <li>Creates backups of files and folders to a specified location</li>
    <li>Supports custom folder categories and extensions</li>
    <li>Easy-to-use, script-based solution for personal file management</li>
    <li>Helps reduce clutter and improves desktop or project folder organization</li>
</ul>

<h2>Tech Stack</h2>
<ul>
    <li><strong>Language:</strong> Python</li>
    <li><strong>Libraries:</strong> <code>os</code>, <code>shutil</code>, <code>datetime</code>, <code>pathlib</code> (all standard Python libraries)</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/Zawadur-Rafid/File_organizer_and_backup.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd File_organizer_and_backup</code></pre>
    </li>
    <li>Ensure you have Python 3 installed. No additional libraries are required.</li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Open the script <code>file_organizer_backup.py</code></li>
    <li>Modify the source folder path (<code>source_path</code>) and backup destination (<code>backup_path</code>) if needed</li>
    <li>Run the script:
        <pre><code>python file_organizer_backup.py</code></pre>
    </li>
    <li>Files will be automatically organized into folders by type, and a backup will be created at the specified location</li>
</ol>

<h2>Folder Structure Example</h2>
<pre><code>Organized_Files/
├── Documents/
├── Images/
├── Videos/
├── Audio/
├── Archives/
└── Others/</code></pre>

<h2>Contributing</h2>
<p>Contributions are welcome! Open issues or submit pull requests to improve functionality, add new features, or optimize performance.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License – see the LICENSE file for details.</p>

</body>
</html>
