function MemoContainer({memo, setMemo}) {
    return <div className="MemoContainer">
        <div>
            <input type="text" className="MemoContainer_title" 
            value={memo.title} />
        </div>
        <div>
            <textarea className="MemoContainer_content" 
            value={memo.content} 
            onchange={(e) => {
                setMemo({
                    ...memo,
                    title: e.target.value
                })
            }} />
        </div>
    </div>
}

export default MemoContainer;