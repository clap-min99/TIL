import MemoList from "./MemoList";

function SideBar({ memos }) {
    return <div className="SideBar">
        <MemoList memos={memos} />
    </div>
}

export default SideBar ;