const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const baseDir = path.resolve(__dirname, '..', '..');
const distLudo = path.join(baseDir, 'dist', 'ludo');
const distSnakes = path.join(baseDir, 'dist', 'snakes');
const outputDir = path.join(baseDir, 'dist_exe');
const iconSrc = path.join(baseDir, 'icon-512.png');

const electronMainCode = `const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');

const gotTheLock = app.requestSingleInstanceLock();
if (!gotTheLock) {
  app.quit();
} else {
  let mainWindow = null;

  function createWindow() {
    mainWindow = new BrowserWindow({
      width: 1280,
      height: 800,
      fullscreen: true,
      autoHideMenuBar: true,
      backgroundColor: '#050c1a',
      icon: path.join(__dirname, 'icon-512.png'),
      webPreferences: {
        nodeIntegration: false,
        contextIsolation: true,
        sandbox: false
      }
    });

    Menu.setApplicationMenu(null);
    mainWindow.loadFile(path.join(__dirname, 'index.html'));

    mainWindow.webContents.on('before-input-event', (event, input) => {
      if (input.key === 'F11' && input.type === 'keyDown') {
        mainWindow.setFullScreen(!mainWindow.isFullScreen());
        event.preventDefault();
      }
      if (input.key === 'Escape' && input.type === 'keyDown' && mainWindow.isFullScreen()) {
        mainWindow.setFullScreen(false);
        event.preventDefault();
      }
    });

    mainWindow.on('closed', () => {
      mainWindow = null;
    });
  }

  app.whenReady().then(createWindow);

  app.on('second-instance', () => {
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore();
      mainWindow.focus();
    }
  });

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
      app.quit();
    }
  });
}
`;

function prepareAndBuild(appDir, appId, productName, artifactName) {
  fs.writeFileSync(path.join(appDir, 'main.js'), electronMainCode, 'utf8');
  if (fs.existsSync(iconSrc)) {
    fs.copyFileSync(iconSrc, path.join(appDir, 'icon-512.png'));
  }
  const pkgConfig = {
    name: appId.toLowerCase(),
    version: '1.0.0',
    description: productName,
    main: 'main.js',
    author: 'Yasin Ullah',
    devDependencies: {
      electron: '33.2.0'
    },
    build: {
      electronVersion: '33.2.0',
      appId: 'com.yasinullah.' + appId,
      productName: productName,
      copyright: 'Copyright \u00a9 2026 Yasin Ullah',
      asar: true,
      directories: {
        output: outputDir
      },
      win: {
        icon: 'icon-512.png',
        target: 'portable'
      },
      portable: {
        artifactName: artifactName
      }
    }
  };
  fs.writeFileSync(path.join(appDir, 'package.json'), JSON.stringify(pkgConfig, null, 2), 'utf8');
  execSync('npx electron-builder --win portable --x64 -c.electronVersion=33.2.0', {
    cwd: appDir,
    stdio: 'inherit',
    env: process.env,
    shell: true
  });
}

function run() {
  fs.mkdirSync(outputDir, { recursive: true });
  prepareAndBuild(distLudo, 'bannuroyaleludo', 'Bannu Royale Ludo', 'BannuRoyaleLudo.exe');
  prepareAndBuild(distSnakes, 'khybersaanpseedhi', 'Khyber Saanp Seedhi Pro', 'KhyberSaanpSeedhi.exe');
}

run();
