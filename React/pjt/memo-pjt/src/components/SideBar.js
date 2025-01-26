import MemoList from "./MemoList";
import SideBarFooter from "./SideBarFooter";
import SideBarHeader from "./SideBarHeader";

function SideBar({ memos }) {
    return (<div className="SideBar">
        <SideBarHeader />
        <MemoList memos={memos} />
        <SideBarFooter />
    </div>)
}

export default SideBar ;