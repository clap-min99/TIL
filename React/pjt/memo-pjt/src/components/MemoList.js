function MemoList({memos}) {
    return (
    <div>
        {memos.map((memo, index) => (
            <div key={index}>
            {memo.title}            
            </div>))}
    </div>
)}

export default MemoList