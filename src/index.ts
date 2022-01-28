import {app, ipcMain, BrowserWindow} from 'electron';

app.whenReady().then(main);

import electronReload from 'electron-reload';
electronReload(__dirname, {}); 

async function main() {
    let mainWindows = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: __dirname + '/preload.js'
        },
        show: false
    });

    mainWindows.loadURL('file://' + __dirname + '/index.html');
    mainWindows.on('ready-to-show', () => {
        mainWindows.show();
    });

}