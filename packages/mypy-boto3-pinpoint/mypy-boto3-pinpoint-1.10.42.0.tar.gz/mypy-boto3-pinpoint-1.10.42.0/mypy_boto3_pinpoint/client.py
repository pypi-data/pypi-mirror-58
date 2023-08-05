"Main interface for pinpoint service Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_pinpoint.client as client_scope
from mypy_boto3_pinpoint.type_defs import (
    ADMChannelRequestTypeDef,
    APNSChannelRequestTypeDef,
    APNSSandboxChannelRequestTypeDef,
    APNSVoipChannelRequestTypeDef,
    APNSVoipSandboxChannelRequestTypeDef,
    BaiduChannelRequestTypeDef,
    CreateAppResponseTypeDef,
    CreateApplicationRequestTypeDef,
    CreateCampaignResponseTypeDef,
    CreateEmailTemplateResponseTypeDef,
    CreateExportJobResponseTypeDef,
    CreateImportJobResponseTypeDef,
    CreateJourneyResponseTypeDef,
    CreatePushTemplateResponseTypeDef,
    CreateSegmentResponseTypeDef,
    CreateSmsTemplateResponseTypeDef,
    CreateVoiceTemplateResponseTypeDef,
    DeleteAdmChannelResponseTypeDef,
    DeleteApnsChannelResponseTypeDef,
    DeleteApnsSandboxChannelResponseTypeDef,
    DeleteApnsVoipChannelResponseTypeDef,
    DeleteApnsVoipSandboxChannelResponseTypeDef,
    DeleteAppResponseTypeDef,
    DeleteBaiduChannelResponseTypeDef,
    DeleteCampaignResponseTypeDef,
    DeleteEmailChannelResponseTypeDef,
    DeleteEmailTemplateResponseTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventStreamResponseTypeDef,
    DeleteGcmChannelResponseTypeDef,
    DeleteJourneyResponseTypeDef,
    DeletePushTemplateResponseTypeDef,
    DeleteSegmentResponseTypeDef,
    DeleteSmsChannelResponseTypeDef,
    DeleteSmsTemplateResponseTypeDef,
    DeleteUserEndpointsResponseTypeDef,
    DeleteVoiceChannelResponseTypeDef,
    DeleteVoiceTemplateResponseTypeDef,
    EmailChannelRequestTypeDef,
    EmailTemplateRequestTypeDef,
    EndpointBatchRequestTypeDef,
    EndpointRequestTypeDef,
    EventsRequestTypeDef,
    ExportJobRequestTypeDef,
    GCMChannelRequestTypeDef,
    GetAdmChannelResponseTypeDef,
    GetApnsChannelResponseTypeDef,
    GetApnsSandboxChannelResponseTypeDef,
    GetApnsVoipChannelResponseTypeDef,
    GetApnsVoipSandboxChannelResponseTypeDef,
    GetAppResponseTypeDef,
    GetApplicationDateRangeKpiResponseTypeDef,
    GetApplicationSettingsResponseTypeDef,
    GetAppsResponseTypeDef,
    GetBaiduChannelResponseTypeDef,
    GetCampaignActivitiesResponseTypeDef,
    GetCampaignDateRangeKpiResponseTypeDef,
    GetCampaignResponseTypeDef,
    GetCampaignVersionResponseTypeDef,
    GetCampaignVersionsResponseTypeDef,
    GetCampaignsResponseTypeDef,
    GetChannelsResponseTypeDef,
    GetEmailChannelResponseTypeDef,
    GetEmailTemplateResponseTypeDef,
    GetEndpointResponseTypeDef,
    GetEventStreamResponseTypeDef,
    GetExportJobResponseTypeDef,
    GetExportJobsResponseTypeDef,
    GetGcmChannelResponseTypeDef,
    GetImportJobResponseTypeDef,
    GetImportJobsResponseTypeDef,
    GetJourneyDateRangeKpiResponseTypeDef,
    GetJourneyExecutionActivityMetricsResponseTypeDef,
    GetJourneyExecutionMetricsResponseTypeDef,
    GetJourneyResponseTypeDef,
    GetPushTemplateResponseTypeDef,
    GetSegmentExportJobsResponseTypeDef,
    GetSegmentImportJobsResponseTypeDef,
    GetSegmentResponseTypeDef,
    GetSegmentVersionResponseTypeDef,
    GetSegmentVersionsResponseTypeDef,
    GetSegmentsResponseTypeDef,
    GetSmsChannelResponseTypeDef,
    GetSmsTemplateResponseTypeDef,
    GetUserEndpointsResponseTypeDef,
    GetVoiceChannelResponseTypeDef,
    GetVoiceTemplateResponseTypeDef,
    ImportJobRequestTypeDef,
    JourneyStateRequestTypeDef,
    ListJourneysResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplatesResponseTypeDef,
    MessageRequestTypeDef,
    NumberValidateRequestTypeDef,
    PhoneNumberValidateResponseTypeDef,
    PushNotificationTemplateRequestTypeDef,
    PutEventStreamResponseTypeDef,
    PutEventsResponseTypeDef,
    RemoveAttributesResponseTypeDef,
    SMSChannelRequestTypeDef,
    SMSTemplateRequestTypeDef,
    SendMessagesResponseTypeDef,
    SendUsersMessageRequestTypeDef,
    SendUsersMessagesResponseTypeDef,
    TagsModelTypeDef,
    UpdateAdmChannelResponseTypeDef,
    UpdateApnsChannelResponseTypeDef,
    UpdateApnsSandboxChannelResponseTypeDef,
    UpdateApnsVoipChannelResponseTypeDef,
    UpdateApnsVoipSandboxChannelResponseTypeDef,
    UpdateApplicationSettingsResponseTypeDef,
    UpdateAttributesRequestTypeDef,
    UpdateBaiduChannelResponseTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateEmailChannelResponseTypeDef,
    UpdateEmailTemplateResponseTypeDef,
    UpdateEndpointResponseTypeDef,
    UpdateEndpointsBatchResponseTypeDef,
    UpdateGcmChannelResponseTypeDef,
    UpdateJourneyResponseTypeDef,
    UpdateJourneyStateResponseTypeDef,
    UpdatePushTemplateResponseTypeDef,
    UpdateSegmentResponseTypeDef,
    UpdateSmsChannelResponseTypeDef,
    UpdateSmsTemplateResponseTypeDef,
    UpdateVoiceChannelResponseTypeDef,
    UpdateVoiceTemplateResponseTypeDef,
    VoiceChannelRequestTypeDef,
    VoiceTemplateRequestTypeDef,
    WriteApplicationSettingsRequestTypeDef,
    WriteCampaignRequestTypeDef,
    WriteEventStreamTypeDef,
    WriteJourneyRequestTypeDef,
    WriteSegmentRequestTypeDef,
)


__all__ = ("PinpointClient",)


class PinpointClient(BaseClient):
    """
    [Pinpoint.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_app(
        self, CreateApplicationRequest: CreateApplicationRequestTypeDef
    ) -> CreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_campaign(
        self, ApplicationId: str, WriteCampaignRequest: WriteCampaignRequestTypeDef
    ) -> CreateCampaignResponseTypeDef:
        """
        [Client.create_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_email_template(
        self, EmailTemplateRequest: EmailTemplateRequestTypeDef, TemplateName: str
    ) -> CreateEmailTemplateResponseTypeDef:
        """
        [Client.create_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_export_job(
        self, ApplicationId: str, ExportJobRequest: ExportJobRequestTypeDef
    ) -> CreateExportJobResponseTypeDef:
        """
        [Client.create_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_export_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_import_job(
        self, ApplicationId: str, ImportJobRequest: ImportJobRequestTypeDef
    ) -> CreateImportJobResponseTypeDef:
        """
        [Client.create_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_journey(
        self, ApplicationId: str, WriteJourneyRequest: WriteJourneyRequestTypeDef
    ) -> CreateJourneyResponseTypeDef:
        """
        [Client.create_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_journey)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_push_template(
        self,
        PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef,
        TemplateName: str,
    ) -> CreatePushTemplateResponseTypeDef:
        """
        [Client.create_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_push_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_segment(
        self, ApplicationId: str, WriteSegmentRequest: WriteSegmentRequestTypeDef
    ) -> CreateSegmentResponseTypeDef:
        """
        [Client.create_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_segment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_sms_template(
        self, SMSTemplateRequest: SMSTemplateRequestTypeDef, TemplateName: str
    ) -> CreateSmsTemplateResponseTypeDef:
        """
        [Client.create_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_sms_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_voice_template(
        self, TemplateName: str, VoiceTemplateRequest: VoiceTemplateRequestTypeDef
    ) -> CreateVoiceTemplateResponseTypeDef:
        """
        [Client.create_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.create_voice_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_adm_channel(self, ApplicationId: str) -> DeleteAdmChannelResponseTypeDef:
        """
        [Client.delete_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_adm_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_apns_channel(self, ApplicationId: str) -> DeleteApnsChannelResponseTypeDef:
        """
        [Client.delete_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_apns_sandbox_channel(
        self, ApplicationId: str
    ) -> DeleteApnsSandboxChannelResponseTypeDef:
        """
        [Client.delete_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_sandbox_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_apns_voip_channel(self, ApplicationId: str) -> DeleteApnsVoipChannelResponseTypeDef:
        """
        [Client.delete_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_apns_voip_sandbox_channel(
        self, ApplicationId: str
    ) -> DeleteApnsVoipSandboxChannelResponseTypeDef:
        """
        [Client.delete_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_sandbox_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_app(self, ApplicationId: str) -> DeleteAppResponseTypeDef:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_baidu_channel(self, ApplicationId: str) -> DeleteBaiduChannelResponseTypeDef:
        """
        [Client.delete_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_baidu_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_campaign(self, ApplicationId: str, CampaignId: str) -> DeleteCampaignResponseTypeDef:
        """
        [Client.delete_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_email_channel(self, ApplicationId: str) -> DeleteEmailChannelResponseTypeDef:
        """
        [Client.delete_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_email_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_email_template(self, TemplateName: str) -> DeleteEmailTemplateResponseTypeDef:
        """
        [Client.delete_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint(self, ApplicationId: str, EndpointId: str) -> DeleteEndpointResponseTypeDef:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_stream(self, ApplicationId: str) -> DeleteEventStreamResponseTypeDef:
        """
        [Client.delete_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_event_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_gcm_channel(self, ApplicationId: str) -> DeleteGcmChannelResponseTypeDef:
        """
        [Client.delete_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_gcm_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_journey(self, ApplicationId: str, JourneyId: str) -> DeleteJourneyResponseTypeDef:
        """
        [Client.delete_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_journey)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_push_template(self, TemplateName: str) -> DeletePushTemplateResponseTypeDef:
        """
        [Client.delete_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_push_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_segment(self, ApplicationId: str, SegmentId: str) -> DeleteSegmentResponseTypeDef:
        """
        [Client.delete_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_segment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_sms_channel(self, ApplicationId: str) -> DeleteSmsChannelResponseTypeDef:
        """
        [Client.delete_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_sms_template(self, TemplateName: str) -> DeleteSmsTemplateResponseTypeDef:
        """
        [Client.delete_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_endpoints(
        self, ApplicationId: str, UserId: str
    ) -> DeleteUserEndpointsResponseTypeDef:
        """
        [Client.delete_user_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_user_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_channel(self, ApplicationId: str) -> DeleteVoiceChannelResponseTypeDef:
        """
        [Client.delete_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_voice_template(self, TemplateName: str) -> DeleteVoiceTemplateResponseTypeDef:
        """
        [Client.delete_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_adm_channel(self, ApplicationId: str) -> GetAdmChannelResponseTypeDef:
        """
        [Client.get_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_adm_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_apns_channel(self, ApplicationId: str) -> GetApnsChannelResponseTypeDef:
        """
        [Client.get_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_apns_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_apns_sandbox_channel(self, ApplicationId: str) -> GetApnsSandboxChannelResponseTypeDef:
        """
        [Client.get_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_apns_sandbox_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_apns_voip_channel(self, ApplicationId: str) -> GetApnsVoipChannelResponseTypeDef:
        """
        [Client.get_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_apns_voip_sandbox_channel(
        self, ApplicationId: str
    ) -> GetApnsVoipSandboxChannelResponseTypeDef:
        """
        [Client.get_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_sandbox_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_app(self, ApplicationId: str) -> GetAppResponseTypeDef:
        """
        [Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_application_date_range_kpi(
        self,
        ApplicationId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> GetApplicationDateRangeKpiResponseTypeDef:
        """
        [Client.get_application_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_application_date_range_kpi)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_application_settings(self, ApplicationId: str) -> GetApplicationSettingsResponseTypeDef:
        """
        [Client.get_application_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_application_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_apps(self, PageSize: str = None, Token: str = None) -> GetAppsResponseTypeDef:
        """
        [Client.get_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_apps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_baidu_channel(self, ApplicationId: str) -> GetBaiduChannelResponseTypeDef:
        """
        [Client.get_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_baidu_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_campaign(self, ApplicationId: str, CampaignId: str) -> GetCampaignResponseTypeDef:
        """
        [Client.get_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_campaign_activities(
        self, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignActivitiesResponseTypeDef:
        """
        [Client.get_campaign_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_activities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_campaign_date_range_kpi(
        self,
        ApplicationId: str,
        CampaignId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> GetCampaignDateRangeKpiResponseTypeDef:
        """
        [Client.get_campaign_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_date_range_kpi)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_campaign_version(
        self, ApplicationId: str, CampaignId: str, Version: str
    ) -> GetCampaignVersionResponseTypeDef:
        """
        [Client.get_campaign_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_campaign_versions(
        self, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignVersionsResponseTypeDef:
        """
        [Client.get_campaign_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_campaigns(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignsResponseTypeDef:
        """
        [Client.get_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_campaigns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_channels(self, ApplicationId: str) -> GetChannelsResponseTypeDef:
        """
        [Client.get_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_channels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_email_channel(self, ApplicationId: str) -> GetEmailChannelResponseTypeDef:
        """
        [Client.get_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_email_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_email_template(self, TemplateName: str) -> GetEmailTemplateResponseTypeDef:
        """
        [Client.get_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_endpoint(self, ApplicationId: str, EndpointId: str) -> GetEndpointResponseTypeDef:
        """
        [Client.get_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_event_stream(self, ApplicationId: str) -> GetEventStreamResponseTypeDef:
        """
        [Client.get_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_event_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_export_job(self, ApplicationId: str, JobId: str) -> GetExportJobResponseTypeDef:
        """
        [Client.get_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_export_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_export_jobs(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetExportJobsResponseTypeDef:
        """
        [Client.get_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_export_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_gcm_channel(self, ApplicationId: str) -> GetGcmChannelResponseTypeDef:
        """
        [Client.get_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_gcm_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_import_job(self, ApplicationId: str, JobId: str) -> GetImportJobResponseTypeDef:
        """
        [Client.get_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_import_jobs(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetImportJobsResponseTypeDef:
        """
        [Client.get_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_import_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_journey(self, ApplicationId: str, JourneyId: str) -> GetJourneyResponseTypeDef:
        """
        [Client.get_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_journey)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_journey_date_range_kpi(
        self,
        ApplicationId: str,
        JourneyId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> GetJourneyDateRangeKpiResponseTypeDef:
        """
        [Client.get_journey_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_journey_date_range_kpi)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_journey_execution_activity_metrics(
        self,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        NextToken: str = None,
        PageSize: str = None,
    ) -> GetJourneyExecutionActivityMetricsResponseTypeDef:
        """
        [Client.get_journey_execution_activity_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_activity_metrics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_journey_execution_metrics(
        self, ApplicationId: str, JourneyId: str, NextToken: str = None, PageSize: str = None
    ) -> GetJourneyExecutionMetricsResponseTypeDef:
        """
        [Client.get_journey_execution_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_metrics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_push_template(self, TemplateName: str) -> GetPushTemplateResponseTypeDef:
        """
        [Client.get_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_push_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_segment(self, ApplicationId: str, SegmentId: str) -> GetSegmentResponseTypeDef:
        """
        [Client.get_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_segment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_segment_export_jobs(
        self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentExportJobsResponseTypeDef:
        """
        [Client.get_segment_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_segment_export_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_segment_import_jobs(
        self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentImportJobsResponseTypeDef:
        """
        [Client.get_segment_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_segment_import_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_segment_version(
        self, ApplicationId: str, SegmentId: str, Version: str
    ) -> GetSegmentVersionResponseTypeDef:
        """
        [Client.get_segment_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_segment_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_segment_versions(
        self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentVersionsResponseTypeDef:
        """
        [Client.get_segment_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_segment_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_segments(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentsResponseTypeDef:
        """
        [Client.get_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_segments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sms_channel(self, ApplicationId: str) -> GetSmsChannelResponseTypeDef:
        """
        [Client.get_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_sms_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sms_template(self, TemplateName: str) -> GetSmsTemplateResponseTypeDef:
        """
        [Client.get_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_sms_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_endpoints(
        self, ApplicationId: str, UserId: str
    ) -> GetUserEndpointsResponseTypeDef:
        """
        [Client.get_user_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_user_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_channel(self, ApplicationId: str) -> GetVoiceChannelResponseTypeDef:
        """
        [Client.get_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_voice_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_voice_template(self, TemplateName: str) -> GetVoiceTemplateResponseTypeDef:
        """
        [Client.get_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.get_voice_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_journeys(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ListJourneysResponseTypeDef:
        """
        [Client.list_journeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.list_journeys)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_templates(
        self,
        NextToken: str = None,
        PageSize: str = None,
        Prefix: str = None,
        TemplateType: str = None,
    ) -> ListTemplatesResponseTypeDef:
        """
        [Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.list_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def phone_number_validate(
        self, NumberValidateRequest: NumberValidateRequestTypeDef
    ) -> PhoneNumberValidateResponseTypeDef:
        """
        [Client.phone_number_validate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.phone_number_validate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_event_stream(
        self, ApplicationId: str, WriteEventStream: WriteEventStreamTypeDef
    ) -> PutEventStreamResponseTypeDef:
        """
        [Client.put_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.put_event_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_events(
        self, ApplicationId: str, EventsRequest: EventsRequestTypeDef
    ) -> PutEventsResponseTypeDef:
        """
        [Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.put_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_attributes(
        self,
        ApplicationId: str,
        AttributeType: str,
        UpdateAttributesRequest: UpdateAttributesRequestTypeDef,
    ) -> RemoveAttributesResponseTypeDef:
        """
        [Client.remove_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.remove_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_messages(
        self, ApplicationId: str, MessageRequest: MessageRequestTypeDef
    ) -> SendMessagesResponseTypeDef:
        """
        [Client.send_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.send_messages)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_users_messages(
        self, ApplicationId: str, SendUsersMessageRequest: SendUsersMessageRequestTypeDef
    ) -> SendUsersMessagesResponseTypeDef:
        """
        [Client.send_users_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.send_users_messages)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, TagsModel: TagsModelTypeDef) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_adm_channel(
        self, ADMChannelRequest: ADMChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateAdmChannelResponseTypeDef:
        """
        [Client.update_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_adm_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_apns_channel(
        self, APNSChannelRequest: APNSChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateApnsChannelResponseTypeDef:
        """
        [Client.update_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_apns_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_apns_sandbox_channel(
        self, APNSSandboxChannelRequest: APNSSandboxChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateApnsSandboxChannelResponseTypeDef:
        """
        [Client.update_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_apns_sandbox_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_apns_voip_channel(
        self, APNSVoipChannelRequest: APNSVoipChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateApnsVoipChannelResponseTypeDef:
        """
        [Client.update_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_apns_voip_sandbox_channel(
        self,
        APNSVoipSandboxChannelRequest: APNSVoipSandboxChannelRequestTypeDef,
        ApplicationId: str,
    ) -> UpdateApnsVoipSandboxChannelResponseTypeDef:
        """
        [Client.update_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_sandbox_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_application_settings(
        self,
        ApplicationId: str,
        WriteApplicationSettingsRequest: WriteApplicationSettingsRequestTypeDef,
    ) -> UpdateApplicationSettingsResponseTypeDef:
        """
        [Client.update_application_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_application_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_baidu_channel(
        self, ApplicationId: str, BaiduChannelRequest: BaiduChannelRequestTypeDef
    ) -> UpdateBaiduChannelResponseTypeDef:
        """
        [Client.update_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_baidu_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_campaign(
        self, ApplicationId: str, CampaignId: str, WriteCampaignRequest: WriteCampaignRequestTypeDef
    ) -> UpdateCampaignResponseTypeDef:
        """
        [Client.update_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_email_channel(
        self, ApplicationId: str, EmailChannelRequest: EmailChannelRequestTypeDef
    ) -> UpdateEmailChannelResponseTypeDef:
        """
        [Client.update_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_email_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_email_template(
        self, EmailTemplateRequest: EmailTemplateRequestTypeDef, TemplateName: str
    ) -> UpdateEmailTemplateResponseTypeDef:
        """
        [Client.update_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_endpoint(
        self, ApplicationId: str, EndpointId: str, EndpointRequest: EndpointRequestTypeDef
    ) -> UpdateEndpointResponseTypeDef:
        """
        [Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_endpoints_batch(
        self, ApplicationId: str, EndpointBatchRequest: EndpointBatchRequestTypeDef
    ) -> UpdateEndpointsBatchResponseTypeDef:
        """
        [Client.update_endpoints_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_endpoints_batch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_gcm_channel(
        self, ApplicationId: str, GCMChannelRequest: GCMChannelRequestTypeDef
    ) -> UpdateGcmChannelResponseTypeDef:
        """
        [Client.update_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_gcm_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_journey(
        self, ApplicationId: str, JourneyId: str, WriteJourneyRequest: WriteJourneyRequestTypeDef
    ) -> UpdateJourneyResponseTypeDef:
        """
        [Client.update_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_journey)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_journey_state(
        self, ApplicationId: str, JourneyId: str, JourneyStateRequest: JourneyStateRequestTypeDef
    ) -> UpdateJourneyStateResponseTypeDef:
        """
        [Client.update_journey_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_journey_state)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_push_template(
        self,
        PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef,
        TemplateName: str,
    ) -> UpdatePushTemplateResponseTypeDef:
        """
        [Client.update_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_push_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_segment(
        self, ApplicationId: str, SegmentId: str, WriteSegmentRequest: WriteSegmentRequestTypeDef
    ) -> UpdateSegmentResponseTypeDef:
        """
        [Client.update_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_segment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_sms_channel(
        self, ApplicationId: str, SMSChannelRequest: SMSChannelRequestTypeDef
    ) -> UpdateSmsChannelResponseTypeDef:
        """
        [Client.update_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_sms_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_sms_template(
        self, SMSTemplateRequest: SMSTemplateRequestTypeDef, TemplateName: str
    ) -> UpdateSmsTemplateResponseTypeDef:
        """
        [Client.update_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_sms_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_voice_channel(
        self, ApplicationId: str, VoiceChannelRequest: VoiceChannelRequestTypeDef
    ) -> UpdateVoiceChannelResponseTypeDef:
        """
        [Client.update_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_voice_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_voice_template(
        self, TemplateName: str, VoiceTemplateRequest: VoiceTemplateRequestTypeDef
    ) -> UpdateVoiceTemplateResponseTypeDef:
        """
        [Client.update_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pinpoint.html#Pinpoint.Client.update_voice_template)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    MethodNotAllowedException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
