const vscode = require('vscode');

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    let showNotification = vscode.commands.registerCommand('jupyter-notifier.showNotification', function (message="This is the default example!") {
        vscode.window.showWarningMessage(message);
    });

    context.subscriptions.push(showNotification);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
}
