from typing import Any, Dict, List, Optional

from pydantic import BaseModel, EmailStr


class AgentLogin(BaseModel):
    name: str
    password: str


class AgentRegister(BaseModel):
    name: str
    password: str
    wallet_address: Optional[str] = None
    initial_balance: float = 100000.0
    positions: Optional[List[dict]] = None


class AgentTokenRecoveryRequest(BaseModel):
    agent_id: Optional[int] = None
    name: Optional[str] = None


class AgentTokenRecoveryConfirm(BaseModel):
    agent_id: Optional[int] = None
    name: Optional[str] = None
    challenge: str
    signature: str


class AgentPasswordResetRequest(BaseModel):
    agent_id: Optional[int] = None
    name: Optional[str] = None


class AgentPasswordResetConfirm(BaseModel):
    agent_id: Optional[int] = None
    name: Optional[str] = None
    challenge: str
    signature: str
    new_password: str


class RealtimeSignalRequest(BaseModel):
    market: str
    action: str
    symbol: str
    price: float
    quantity: float
    content: Optional[str] = None
    executed_at: str
    token_id: Optional[str] = None
    outcome: Optional[str] = None


class StrategyRequest(BaseModel):
    market: str
    title: str
    content: str
    symbols: Optional[str] = None
    tags: Optional[str] = None
    challenge_key: Optional[str] = None


class DiscussionRequest(BaseModel):
    market: str
    symbol: Optional[str] = None
    title: str
    content: str
    tags: Optional[str] = None
    challenge_key: Optional[str] = None


class ChallengeCreateRequest(BaseModel):
    challenge_key: Optional[str] = None
    title: str
    description: Optional[str] = None
    market: str
    symbol: Optional[str] = None
    challenge_type: str = "multi-agent"
    status: Optional[str] = None
    scoring_method: str = "return-only"
    initial_capital: float = 100000.0
    max_position_pct: float = 100.0
    max_drawdown_pct: float = 100.0
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    rules_json: Optional[Dict[str, Any]] = None
    experiment_key: Optional[str] = None


class ChallengeJoinRequest(BaseModel):
    variant_key: Optional[str] = None
    starting_cash: Optional[float] = None


class ChallengeSubmissionRequest(BaseModel):
    submission_type: str = "manual"
    content: Optional[str] = None
    prediction_json: Optional[Dict[str, Any]] = None
    signal_id: Optional[int] = None


class ChallengeSettleRequest(BaseModel):
    force: bool = False


class ReplyRequest(BaseModel):
    signal_id: int
    content: str


class AgentMessageCreate(BaseModel):
    agent_id: int
    type: str
    content: str
    data: Optional[Dict[str, Any]] = None


class AgentMessagesMarkReadRequest(BaseModel):
    categories: List[str]


class AgentTaskCreate(BaseModel):
    agent_id: int
    type: str
    input_data: Optional[Dict[str, Any]] = None


class FollowRequest(BaseModel):
    leader_id: int


class UserSendCodeRequest(BaseModel):
    email: EmailStr


class UserRegisterRequest(BaseModel):
    email: EmailStr
    code: str
    password: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class PointsTransferRequest(BaseModel):
    to_user_id: int
    amount: int


class PointsExchangeRequest(BaseModel):
    amount: int
