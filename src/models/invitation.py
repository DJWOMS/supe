import datetime
import edgy

from .base import BaseModel

from src.apps.invitation.constants import StatusInvitation


class InvitationModel(BaseModel):

    code: str = edgy.CharField(unique=True, max_length=255)
    status: StatusInvitation = edgy.ChoiceField(
        choices=StatusInvitation,
        default=StatusInvitation.ACTIVE
    )
    date_valid_at: datetime.date = edgy.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        tablename = "invitations"
