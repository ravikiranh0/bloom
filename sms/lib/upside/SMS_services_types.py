################################################## 
# SMS_services_types.py 
# generated by ZSI.generate.wsdl2python
##################################################


import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

##############################
# targetNamespace
# http://upsidewireless.com/webservice/sms
##############################

class upsidewireless_com_webservice_sms:
    targetNamespace = "http://upsidewireless.com/webservice/sms"

    class SmsEncoding_(ZSI.TC.String, TypeDefinition):
        schema = "http://upsidewireless.com/webservice/sms"
        type = (schema, "SmsEncoding")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class SMSSendResult_(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://upsidewireless.com/webservice/sms"
        type = (schema, "SMSSendResult")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = upsidewireless_com_webservice_sms.SMSSendResult_.schema
            TClist = [ZSI.TC.Boolean(pname=(ns,"isOk"), aname="isOk", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"trackingId"), aname="trackingId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"number"), aname="number", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"convertedNumber"), aname="convertedNumber", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"deferUntilOccursInThePast"), aname="deferUntilOccursInThePast", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"messageIsEmpty"), aname="messageIsEmpty", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"tooManyMessages"), aname="tooManyMessages", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"invalidCountryCode"), aname="invalidCountryCode", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"isBlocked"), aname="isBlocked", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"BlockedReason"), aname="BlockedReason", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.isOk = None
                    self.trackingId = None
                    self.number = None
                    self.convertedNumber = None
                    self.deferUntilOccursInThePast = None
                    self.messageIsEmpty = None
                    self.tooManyMessages = None
                    self.invalidCountryCode = None
                    self.isBlocked = None
                    self.BlockedReason = None
                    return
            Holder.__name__ = "SMSSendResult_Holder"
            self.pyclass = Holder

    class Send_Test(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_Test"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_Test.schema
            TClist = [ZSI.TC.String(pname=(ns,"token"), aname="token", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"signature"), aname="signature", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"recipient"), aname="recipient", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"message"), aname="message", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://upsidewireless.com/webservice/sms","SmsEncoding",lazy=False)(pname=(ns,"encoding"), aname="encoding", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_Test")
            kw["aname"] = "Send_Test"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.token = None
                    self.signature = None
                    self.recipient = None
                    self.message = None
                    self.encoding = None
                    return
            Holder.__name__ = "Send_Test_Holder"
            self.pyclass = Holder

    class Send_TestResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_TestResponse"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_TestResponse.schema
            TClist = [GTD("http://upsidewireless.com/webservice/sms","SMSSendResult",lazy=False)(pname=(ns,"Send_TestResult"), aname="Send_TestResult", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_TestResponse")
            kw["aname"] = "Send_TestResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.Send_TestResult = None
                    return
            Holder.__name__ = "Send_TestResponse_Holder"
            self.pyclass = Holder

    class Send_Plain(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_Plain"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_Plain.schema
            TClist = [ZSI.TC.String(pname=(ns,"token"), aname="token", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"signature"), aname="signature", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"recipient"), aname="recipient", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"message"), aname="message", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://upsidewireless.com/webservice/sms","SmsEncoding",lazy=False)(pname=(ns,"encoding"), aname="encoding", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_Plain")
            kw["aname"] = "Send_Plain"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.token = None
                    self.signature = None
                    self.recipient = None
                    self.message = None
                    self.encoding = None
                    return
            Holder.__name__ = "Send_Plain_Holder"
            self.pyclass = Holder

    class Send_PlainResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_PlainResponse"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_PlainResponse.schema
            TClist = [GTD("http://upsidewireless.com/webservice/sms","SMSSendResult",lazy=False)(pname=(ns,"Send_PlainResult"), aname="Send_PlainResult", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_PlainResponse")
            kw["aname"] = "Send_PlainResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.Send_PlainResult = None
                    return
            Holder.__name__ = "Send_PlainResponse_Holder"
            self.pyclass = Holder

    class Send_Plain_Dedicated(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_Plain_Dedicated"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_Plain_Dedicated.schema
            TClist = [ZSI.TC.String(pname=(ns,"token"), aname="token", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"signature"), aname="signature", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"recipient"), aname="recipient", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"message"), aname="message", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://upsidewireless.com/webservice/sms","SmsEncoding",lazy=False)(pname=(ns,"encoding"), aname="encoding", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"carrierCode"), aname="carrierCode", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"dedicatedNumber"), aname="dedicatedNumber", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.FPdouble(pname=(ns,"tariff"), aname="tariff", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_Plain_Dedicated")
            kw["aname"] = "Send_Plain_Dedicated"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.token = None
                    self.signature = None
                    self.recipient = None
                    self.message = None
                    self.encoding = None
                    self.carrierCode = None
                    self.dedicatedNumber = None
                    self.tariff = None
                    return
            Holder.__name__ = "Send_Plain_Dedicated_Holder"
            self.pyclass = Holder

    class Send_Plain_DedicatedResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_Plain_DedicatedResponse"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_Plain_DedicatedResponse.schema
            TClist = [GTD("http://upsidewireless.com/webservice/sms","SMSSendResult",lazy=False)(pname=(ns,"Send_Plain_DedicatedResult"), aname="Send_Plain_DedicatedResult", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_Plain_DedicatedResponse")
            kw["aname"] = "Send_Plain_DedicatedResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.Send_Plain_DedicatedResult = None
                    return
            Holder.__name__ = "Send_Plain_DedicatedResponse_Holder"
            self.pyclass = Holder

    class Send_Plain_Deferred(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_Plain_Deferred"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_Plain_Deferred.schema
            TClist = [ZSI.TC.String(pname=(ns,"token"), aname="token", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"signature"), aname="signature", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"recipient"), aname="recipient", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"message"), aname="message", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://upsidewireless.com/webservice/sms","SmsEncoding",lazy=False)(pname=(ns,"encoding"), aname="encoding", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"DelayHours"), aname="DelayHours", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"DelayMinutes"), aname="DelayMinutes", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"label"), aname="label", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_Plain_Deferred")
            kw["aname"] = "Send_Plain_Deferred"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.token = None
                    self.signature = None
                    self.recipient = None
                    self.message = None
                    self.encoding = None
                    self.DelayHours = None
                    self.DelayMinutes = None
                    self.label = None
                    return
            Holder.__name__ = "Send_Plain_Deferred_Holder"
            self.pyclass = Holder

    class Send_Plain_DeferredResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_Plain_DeferredResponse"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_Plain_DeferredResponse.schema
            TClist = [GTD("http://upsidewireless.com/webservice/sms","SMSSendResult",lazy=False)(pname=(ns,"Send_Plain_DeferredResult"), aname="Send_Plain_DeferredResult", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_Plain_DeferredResponse")
            kw["aname"] = "Send_Plain_DeferredResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.Send_Plain_DeferredResult = None
                    return
            Holder.__name__ = "Send_Plain_DeferredResponse_Holder"
            self.pyclass = Holder

    class Send_Flash(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_Flash"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_Flash.schema
            TClist = [ZSI.TC.String(pname=(ns,"token"), aname="token", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"signature"), aname="signature", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"recipient"), aname="recipient", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"message"), aname="message", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_Flash")
            kw["aname"] = "Send_Flash"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.token = None
                    self.signature = None
                    self.recipient = None
                    self.message = None
                    return
            Holder.__name__ = "Send_Flash_Holder"
            self.pyclass = Holder

    class Send_FlashResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_FlashResponse"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_FlashResponse.schema
            TClist = [GTD("http://upsidewireless.com/webservice/sms","SMSSendResult",lazy=False)(pname=(ns,"Send_FlashResult"), aname="Send_FlashResult", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_FlashResponse")
            kw["aname"] = "Send_FlashResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.Send_FlashResult = None
                    return
            Holder.__name__ = "Send_FlashResponse_Holder"
            self.pyclass = Holder

    class Send_WAPPush(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_WAPPush"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_WAPPush.schema
            TClist = [ZSI.TC.String(pname=(ns,"token"), aname="token", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"signature"), aname="signature", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"recipient"), aname="recipient", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"title"), aname="title", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"url"), aname="url", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_WAPPush")
            kw["aname"] = "Send_WAPPush"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.token = None
                    self.signature = None
                    self.recipient = None
                    self.title = None
                    self.url = None
                    return
            Holder.__name__ = "Send_WAPPush_Holder"
            self.pyclass = Holder

    class Send_WAPPushResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Send_WAPPushResponse"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            ns = upsidewireless_com_webservice_sms.Send_WAPPushResponse.schema
            TClist = [GTD("http://upsidewireless.com/webservice/sms","SMSSendResult",lazy=False)(pname=(ns,"Send_WAPPushResult"), aname="Send_WAPPushResult", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","Send_WAPPushResponse")
            kw["aname"] = "Send_WAPPushResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.Send_WAPPushResult = None
                    return
            Holder.__name__ = "Send_WAPPushResponse_Holder"
            self.pyclass = Holder

    class SMSSendResult(ElementDeclaration):
        literal = "SMSSendResult"
        schema = "http://upsidewireless.com/webservice/sms"
        def __init__(self, **kw):
            kw["pname"] = ("http://upsidewireless.com/webservice/sms","SMSSendResult")
            kw["aname"] = "SMSSendResult"
            if upsidewireless_com_webservice_sms.SMSSendResult_ not in upsidewireless_com_webservice_sms.SMSSendResult.__bases__:
                bases = list(upsidewireless_com_webservice_sms.SMSSendResult.__bases__)
                bases.insert(0, upsidewireless_com_webservice_sms.SMSSendResult_)
                upsidewireless_com_webservice_sms.SMSSendResult.__bases__ = tuple(bases)

            upsidewireless_com_webservice_sms.SMSSendResult_.__init__(self, **kw)
            if self.pyclass is not None: self.pyclass.__name__ = "SMSSendResult_Holder"

# end class upsidewireless_com_webservice_sms (tns: http://upsidewireless.com/webservice/sms)
