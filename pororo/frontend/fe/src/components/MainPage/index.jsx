import { useNavigate } from "react-router-dom";
import "./index.css";

const MainPage = () => {
    const navigate = useNavigate();

    return (
        <div className="main-page">
            <div className="card-container">
                {/* 왼쪽 카드 */}
                <div
                    className="card single-mode"
                    onClick={() => navigate("/single")}
                >
                    <h2>즐거운 발음 학습하기</h2>
                    <p>
                        발음 익히기, 단어 게임, 가상의 친구와 즐겁게 대화하며
                        재미있게 발음을 학습해요!
                    </p>
                </div>

                {/* 오른쪽 카드 */}
                <div
                    className="card multi-mode"
                    onClick={() => navigate("/multi")}
                >
                    <h2>선생님과 단어 놀이</h2>
                    <p>
                        선생님과 친구들과의 영상 단어 카드 놀이를 통해 다양한
                        단어들을 직접 말해봐요!
                    </p>
                </div>
            </div>
        </div>
    );
};

export default MainPage;
