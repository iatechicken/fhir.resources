# _*_ coding: utf-8 _*_
"""Validators for ``pydantic`` Custom DataType"""
import importlib
from pathlib import Path
from typing import Union

from pydantic.class_validators import make_generic_validator
from pydantic.types import StrBytes

from .fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

MODEL_CLASSES = {
    "Element": (None, ".element"),
    "Resource": (None, ".resource"),
    "DomainResource": (None, ".domainresource"),
    "BackboneElement": (None, ".backboneelement"),
    "Extension": (None, ".extension"),
    "Meta": (None, ".meta"),
    "Narrative": (None, ".narrative"),
    "Address": (None, ".address"),
    "Period": (None, ".period"),
    "Attachment": (None, ".attachment"),
    "CodeableConcept": (None, ".codeableconcept"),
    "Coding": (None, ".coding"),
    "ContactPoint": (None, ".contactpoint"),
    "HumanName": (None, ".humanname"),
    "Identifier": (None, ".identifier"),
    "Reference": (None, ".reference"),
    "Quantity": (None, ".quantity"),
    "Range": (None, ".range"),
    "Ratio": (None, ".ratio"),
    "Signature": (None, ".signature"),
    "Timing": (None, ".timing"),
    "TimingRepeat": (None, ".timing"),
    "Duration": (None, ".duration"),
}


def get_fhir_model_class(model_name: str) -> FHIRAbstractModel:
    """
    """
    global MODEL_CLASSES
    klass, module_name = MODEL_CLASSES[model_name]
    if klass is not None:
        return klass
    module = importlib.import_module(module_name, package=__package__)
    klass = getattr(module, model_name)
    MODEL_CLASSES[model_name] = (klass, module_name)
    return klass


def run_validator_for_fhir_type(model_type_cls, v, values, config, field):
    """ """
    cls = get_fhir_model_class(model_type_cls.__resource_type__)
    for validator in model_type_cls.__get_validators__():
        func = make_generic_validator(validator)
        v = func(cls, v, values, config, field)
    return v


def fhir_model_validator(
    model_name: str, v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    """ """
    model_class = get_fhir_model_class(model_name)
    if isinstance(v, (str, bytes)):
        v = model_class.parse_raw(v)
    elif isinstance(v, Path):
        v = model_class.parse_file(v)
    elif isinstance(v, dict):
        v = model_class.parse_obj(v)
    if not isinstance(v, FHIRAbstractModel):
        raise ValueError()
    if model_name != v.resource_type:
        raise ValueError
    return v


def element_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):

    return fhir_model_validator("Element", v)


def resource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):

    return fhir_model_validator("Resource", v)


def domainresource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):

    return fhir_model_validator("DomainResource", v)


def backboneelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BackboneElement", v)


def extension_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Extension", v)


def meta_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Meta", v)


def narrative_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Narrative", v)


def address_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Address", v)


def period_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Period", v)


def attachment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Attachment", v)


def codeableconcept_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeableConcept", v)


def coding_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Coding", v)


def contactpoint_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContactPoint", v)


def humanname_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("HumanName", v)


def identifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Identifier", v)


def reference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Reference", v)


def quantity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Quantity", v)


def range_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Range", v)


def ratio_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Ratio", v)


def signature_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Signature", v)


def timing_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Timing", v)


def timingrepeat_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TimingRepeat", v)


def duration_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Duration", v)


__all__ = [
    "element_validator",
    "resource_validator",
    "domainresource_validator",
    "backboneelement_validator",
    "extension_validator",
    "meta_validator",
    "narrative_validator",
    "address_validator",
    "period_validator",
    "attachment_validator",
    "codeableconcept_validator",
    "coding_validator",
    "contactpoint_validator",
    "humanname_validator",
    "identifier_validator",
    "reference_validator",
    "quantity_validator",
    "range_validator",
    "ratio_validator",
    "signature_validator",
    "timing_validator",
    "timingrepeat_validator",
    "duration_validator",
]