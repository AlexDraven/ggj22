import {app, ipcMain, BrowserWindow} from 'electron';

//app.on('ready', initWindows);
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
   // mainWindows.webContents.openDevTools();
    mainWindows.on('ready-to-show', () => {
        mainWindows.show();
    });

}