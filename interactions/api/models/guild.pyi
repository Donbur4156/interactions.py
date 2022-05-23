from datetime import datetime
from enum import Enum, IntEnum
from typing import Any, Dict, List, Optional, Union

from .attrs_utils import DictSerializerMixin, ClientSerializerMixin, define
from .channel import Channel as Channel, ChannelType as ChannelType, Thread as Thread
from .member import Member as Member
from .message import Emoji as Emoji, Sticker as Sticker
from .misc import Image, Overwrite, Snowflake
from .presence import PresenceActivity as PresenceActivity
from .role import Role as Role
from .team import Application as Application
from .user import User as User


class VerificationLevel(IntEnum):
    NONE: int
    LOW: int
    MEDIUM: int
    HIGH: int
    VERY_HIGH: int

class ExplicitContentFilterLevel(IntEnum):
    DISABLED: int
    MEMBERS_WITHOUT_ROLES: int
    ALL_MEMBERS: int

class DefaultMessageNotificationLevel(IntEnum):
    ALL_MESSAGES: int
    ONLY_MENTIONS: int

class EntityType(IntEnum):
    STAGE_INSTANCE: int
    VOICE: int
    EXTERNAL: int

class EventStatus(IntEnum):
    SCHEDULED: int
    ACTIVE: int
    COMPLETED: int
    CANCELED: int

class InviteTargetType(IntEnum):
    STREAM: int
    EMBEDDED_APPLICATION: int

class GuildFeatures(Enum):
    ANIMATED_BANNER: str
    ANIMATED_ICON: str
    BANNER: str
    COMMERCE: str
    COMMUNITY: str
    DISCOVERABLE: str
    FEATURABLE: str
    INVITE_SPLASH: str
    MEMBER_VERIFICATION_GATE_ENABLED: str
    MONETIZATION_ENABLED: str
    MORE_STICKERS: str
    NEWS: str
    PARTNERED: str
    PREVIEW_ENABLED: str
    PRIVATE_THREADS: str
    ROLE_ICONS: str
    TICKETED_EVENTS_ENABLED: str
    VANITY_URL: str
    VERIFIED: str
    VIP_REGIONS: str
    WELCOME_SCREEN_ENABLED: str


@define()
class WelcomeChannels(DictSerializerMixin):
    channel_id: int
    description: str
    emoji_id: Optional[Snowflake]
    emoji_name: Optional[str]


@define()
class WelcomeScreen(DictSerializerMixin):
    description: Optional[str]
    welcome_channels: Optional[List[WelcomeChannels]]


@define()
class StageInstance(DictSerializerMixin):
    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    topic: str
    privacy_level: int
    discoverable_disabled: bool


@define()
class UnavailableGuild(DictSerializerMixin):
    id: Snowflake
    unavailable: bool


@define()
class Guild(ClientSerializerMixin):
    id: Snowflake
    name: str
    icon: Optional[str]
    icon_hash: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: Optional[bool]
    owner_id: Snowflake
    permissions: Optional[str]
    region: Optional[str]
    afk_channel_id: Optional[Snowflake]
    afk_timeout: Optional[int]
    widget_enabled: Optional[bool]
    widget_channel_id: Optional[Snowflake]
    verification_level: int
    default_message_notifications: int
    explicit_content_filter: int
    roles: List[Role]
    emojis: List[Emoji]
    mfa_level: int
    application_id: Optional[Snowflake]
    system_channel_id: Optional[Snowflake]
    system_channel_flags: int
    rules_channel_id: Optional[Snowflake]
    joined_at: Optional[datetime]
    large: Optional[bool]
    unavailable: Optional[bool]
    member_count: Optional[int]
    members: Optional[List[Member]]
    channels: Optional[List[Channel]]
    threads: Optional[List[Thread]]
    presences: Optional[List[PresenceActivity]]
    max_presences: Optional[int]
    max_members: Optional[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: int
    premium_subscription_count: Optional[int]
    preferred_locale: str
    public_updates_channel_id: Optional[Snowflake]
    max_video_channel_users: Optional[int]
    approximate_member_count: Optional[int]
    approximate_presence_count: Optional[int]
    welcome_screen: Optional[WelcomeScreen]
    nsfw_level: int
    stage_instances: Optional[List[StageInstance]]
    stickers: Optional[List[Sticker]]
    features: List[str]
    async def ban(self, member_id: int, reason: Optional[str] = ..., delete_message_days: Optional[int] = ...) -> None: ...
    async def remove_ban(self, user_id: int, reason: Optional[str] = ...) -> None: ...
    async def kick(self, member_id: int, reason: Optional[str] = ...) -> None: ...
    async def add_member_role(self, role: Union[Role, int], member_id: int, reason: Optional[str] = ...) -> None: ...
    async def remove_member_role(self, role: Union[Role, int], member_id: int, reason: Optional[str] = ...) -> None: ...
    async def create_role(self, name: str, color: Optional[int] = ..., hoist: Optional[bool] = ..., mentionable: Optional[bool] = ..., reason: Optional[str] = ...) -> Role: ...
    async def get_member(self, member_id: int) -> Member: ...
    async def delete_channel(self, channel_id: int) -> None: ...
    async def delete_role(self, role_id: int, reason: Optional[str] = ...) -> None: ...
    async def modify_role(self, role_id: int, name: Optional[str] = ..., color: Optional[int] = ..., hoist: Optional[bool] = ..., mentionable: Optional[bool] = ..., reason: Optional[str] = ...) -> Role: ...
    async def create_thread(self, name: str, channel_id: int, type: Optional[ChannelType] = ..., auto_archive_duration: Optional[int] = ..., invitable: Optional[bool] = ..., message_id: Optional[int] = ..., reason: Optional[str] = ...) -> Channel: ...
    async def create_channel(self, name: str, type: ChannelType, topic: Optional[str] = ..., bitrate: Optional[int] = ..., user_limit: Optional[int] = ..., rate_limit_per_user: Optional[int] = ..., position: Optional[int] = ..., permission_overwrites: Optional[List[Overwrite]] = ..., parent_id: Optional[int] = ..., nsfw: Optional[bool] = ..., reason: Optional[str] = ...) -> Channel: ...
    async def modify_channel(self, channel_id: int, name: Optional[str] = ..., topic: Optional[str] = ..., bitrate: Optional[int] = ..., user_limit: Optional[int] = ..., rate_limit_per_user: Optional[int] = ..., position: Optional[int] = ..., permission_overwrites: Optional[List[Overwrite]] = ..., parent_id: Optional[int] = ..., nsfw: Optional[bool] = ..., archived: Optional[bool] = ..., auto_archive_duration: Optional[int] = ..., locked: Optional[bool] = ..., reason: Optional[str] = ...) -> Channel: ...
    async def modify_member(self, member_id: int, nick: Optional[str] = ..., roles: Optional[List[int]] = ..., mute: Optional[bool] = ..., deaf: Optional[bool] = ..., channel_id: Optional[int] = ..., communication_disabled_until: Optional[datetime.isoformat] = ..., reason: Optional[str] = ...) -> Member: ...
    async def get_preview(self) -> GuildPreview: ...
    async def leave(self) -> None: ...
    async def modify(self, name: Optional[str] = ..., verification_level: Optional[VerificationLevel] = ..., default_message_notifications: Optional[DefaultMessageNotificationLevel] = ..., explicit_content_filter: Optional[ExplicitContentFilterLevel] = ..., afk_channel_id: Optional[int] = ..., afk_timeout: Optional[int] = ..., icon: Optional[Image] = ..., owner_id: Optional[int] = ..., splash: Optional[Image] = ..., discovery_splash: Optional[Image] = ..., banner: Optional[Image] = ..., system_channel_id: Optional[int] = ..., suppress_join_notifications: Optional[bool] = ..., suppress_premium_subscriptions: Optional[bool] = ..., suppress_guild_reminder_notifications: Optional[bool] = ..., suppress_join_notification_replies: Optional[bool] = ..., rules_channel_id: Optional[int] = ..., public_updates_channel_id: Optional[int] = ..., preferred_locale: Optional[str] = ..., description: Optional[str] = ..., premium_progress_bar_enabled: Optional[bool] = ..., reason: Optional[str] = ...) -> Guild: ...
    async def set_name(self, name: str, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_verification_level(self, verification_level: VerificationLevel, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_default_message_notifications(self, default_message_notifications: DefaultMessageNotificationLevel, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_explicit_content_filter(self, explicit_content_filter: ExplicitContentFilterLevel, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_afk_channel(self, afk_channel_id: int, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_afk_timeout(self, afk_timeout: int, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_system_channel(self, system_channel_id: int, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_rules_channel(self, rules_channel_id: int, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_public_updates_channel(self, public_updates_channel_id: int, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_preferred_locale(self, preferred_locale: str, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_description(self, description: str, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_premium_progress_bar_enabled(self, premium_progress_bar_enabled: bool, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_icon(self, icon: Image, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_splash(self, splash: Image, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_discovery_splash(self, discovery_splash: Image, *, reason: Optional[str] = ...) -> Guild: ...
    async def set_banner(self, banner: Image, *, reason: Optional[str] = ...) -> Guild: ...
    async def create_scheduled_event(self, name: str, entity_type: EntityType, scheduled_start_time: datetime.isoformat, scheduled_end_time: Optional[datetime.isoformat] = ..., entity_metadata: Optional['EventMetadata'] = ..., channel_id: Optional[int] = ..., description: Optional[str] = ..., image: Optional[Image] = ...) -> ScheduledEvents: ...
    async def modify_scheduled_event(self, event_id: int, name: Optional[str] = ..., entity_type: Optional[EntityType] = ..., scheduled_start_time: Optional[datetime.isoformat] = ..., scheduled_end_time: Optional[datetime.isoformat] = ..., entity_metadata: Optional['EventMetadata'] = ..., channel_id: Optional[int] = ..., description: Optional[str] = ..., status: Optional[EventStatus] = ..., image: Optional[Image] = ...) -> ScheduledEvents: ...
    async def delete_scheduled_event(self, event_id: int) -> None: ...
    async def get_all_channels(self) -> List[Channel]: ...
    async def get_all_roles(self) -> List[Role]: ...
    async def get_role(self, role_id: int) -> Role: ...
    async def modify_role_position(self, role_id: Union[Role, int], position: int, reason: Optional[str] = ...) -> List[Role]: ...
    async def modify_role_positions(self, changes: List[dict], reason: Optional[str] = ...) -> List[Role]: ...
    async def get_bans(self, limit: Optional[int] = ..., before: Optional[int] = ..., after: Optional[int] = ...) -> List[Dict[str, User]]: ...
    async def get_all_bans(self) -> List[Dict[str, User]]: ...
    async def get_emoji(self, emoji_id: int) -> Emoji: ...
    async def get_all_emoji(self) -> List[Emoji]: ...
    async def create_emoji(self, image: Image, name: Optional[str] = ..., roles: Optional[Union[List[Role], List[int]]] = ..., reason: Optional[str] = ...) -> Emoji: ...
    async def delete_emoji(self, emoji: Union[Emoji, int], reason: Optional[str] = ...) -> None: ...
    async def get_list_of_members(self, limit: Optional[int] = ..., after: Optional[Union[Member, int]] = ...) -> List[Member]: ...
    async def search_members(self, query: str, limit: Optional[int] = ...) -> List[Member]: ...
    async def get_all_members(self) -> List[Member]: ...
    @property
    def icon_url(self) -> Optional[str]: ...
    @property
    def banner_url(self) -> Optional[str]: ...
    @property
    def splash_url(self) -> Optional[str]: ...
    @property
    def discovery_splash_url(self) -> Optional[str]: ...


@define()
class GuildPreview(DictSerializerMixin):
    id: Snowflake
    emojis: Optional[List[Emoji]]
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    features: Optional[List[str]]
    approximate_member_count: int
    approximate_presence_count: int
    description: Optional[str]


@define()
class Integration(DictSerializerMixin):
    id: Snowflake
    name: str
    type: str
    enabled: bool
    syncing: bool
    role_id: Snowflake
    enable_emoticons: bool
    expire_behavior: int
    expire_grace_period: int
    user: User
    account: Any
    synced_at: datetime
    subscriber_count: int
    revoked: bool
    application: Application


@define()
class Invite(ClientSerializerMixin):
    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: datetime
    expires_at: datetime
    type: int
    inviter: User
    code: str
    guild_id: Optional[Snowflake]
    channel_id: Optional[Snowflake]
    target_user_type: Optional[int]
    target_user: Optional[User]
    target_type: Optional[int]
    guild: Optional[Guild]
    channel: Optional[Channel]
    async def delete(self) -> None: ...


@define()
class GuildTemplate(DictSerializerMixin):
    code: str
    name: str
    description: Optional[str]
    usage_count: int
    creator_id: Snowflake
    creator: User
    created_at: datetime
    updated_at: datetime
    source_guild_id: Snowflake
    serialized_source_guild: Guild
    is_dirty: Optional[bool]


@define()
class EventMetadata(DictSerializerMixin):
    location: Optional[str]


@define()
class ScheduledEvents(DictSerializerMixin):
    id: Snowflake
    guild_id: Snowflake
    channel_id: Optional[Snowflake]
    creator_id: Optional[Snowflake]
    name: str
    description: str
    scheduled_start_time: Optional[datetime]
    scheduled_end_time: Optional[datetime]
    privacy_level: int
    entity_type: int
    entity_id: Optional[Snowflake]
    entity_metadata: Optional[EventMetadata]
    creator: Optional[User]
    user_count: Optional[int]
    status: int
    image: Optional[str]
