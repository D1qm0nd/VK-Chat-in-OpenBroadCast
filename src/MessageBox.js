import './MessageBox.css'

function MessageBox({children}) {
    return (
        <div className="MessageBox">
            {children}
        </div>
    );
}

export default MessageBox;