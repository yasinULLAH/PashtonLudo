const fs = require('fs');
const path = require('path');
const builder = require('electron-builder');

const baseDir = path.resolve(__dirname, '..', '..');
const distLudo = path.join(baseDir, 'dist', 'ludo');
const distSnakes = path.join(baseDir, 'dist', 'snakes');
const outputDir = path.join(baseDir, 'dist_exe');
const faviconPath = path.join(baseDir, 'favicon.ico');

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
      icon: path.join(__dirname, 'favicon.ico'),
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

async function buildApp(appDir, appId, productName, artifactName) {
  fs.writeFileSync(path.join(appDir, 'main.js'), electronMainCode, 'utf8');
  if (fs.existsSync(faviconPath)) {
    fs.copyFileSync(faviconPath, path.join(appDir, 'favicon.ico'));
  }
  fs.writeFileSync(
    path.join(appDir, 'package.json'),
    JSON.stringify({
      name: appId.toLowerCase(),
      version: '1.0.0',
      description: productName,
      main: 'main.js',
      author: 'Yasin Ullah',
      devDependencies: {
        electron: '33.2.0'
      }
    }, null, 2),
    'utf8'
  );

  await builder.build({
    targets: builder.Platform.WINDOWS.createTargets(['portable'], builder.Arch.x64),
    config: {
      appId: 'com.yasinullah.' + appId,
      productName: productName,
      copyright: 'Copyright © 2026 Yasin Ullah',
      asar: true,
      directories: {
        app: appDir,
        output: outputDir
      },
      win: {
        icon: path.join(appDir, 'favicon.ico'),
        target: 'portable'
      },
      portable: {
        artifactName: artifactName
      }
    }
  });
}

async function run() {
  await buildApp(distLudo, 'bannuroyaleludo', 'Bannu Royale Ludo', 'BannuRoyaleLudo.exe');
  await buildApp(distSnakes, 'khybersaanpseedhi', 'Khyber Saanp Seedhi Pro', 'KhyberSaanpSeedhi.exe');
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
