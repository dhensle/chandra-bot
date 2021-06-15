# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chandra_bot_data_model.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="chandra_bot_data_model.proto",
    package="chandra_bot_data_model",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x1c\x63handra_bot_data_model.proto\x12\x16\x63handra_bot_data_model",\n\x0b\x41\x66\x66iliation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61liases\x18\x02 \x03(\t"\xa4\x02\n\x05Human\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61liases\x18\x02 \x03(\t\x12\x0f\n\x07hash_id\x18\x03 \x01(\t\x12@\n\x13\x63urrent_affiliation\x18\x04 \x01(\x0b\x32#.chandra_bot_data_model.Affiliation\x12\x41\n\x14previous_affiliation\x18\x05 \x03(\x0b\x32#.chandra_bot_data_model.Affiliation\x12\x44\n\x17last_degree_affiliation\x18\x06 \x01(\x0b\x32#.chandra_bot_data_model.Affiliation\x12\x11\n\torcid_url\x18\x07 \x01(\t\x12\r\n\x05orcid\x18\x08 \x01(\t"\xb9\x03\n\x05Paper\x12\x0e\n\x06number\x18\x01 \x01(\t\x12/\n\x07\x61uthors\x18\x02 \x03(\x0b\x32\x1e.chandra_bot_data_model.Author\x12/\n\x07reviews\x18\x03 \x03(\x0b\x32\x1e.chandra_bot_data_model.Review\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\x12Q\n\x1f\x63ommittee_presentation_decision\x18\x06 \x01(\x0e\x32(.chandra_bot_data_model.PRESENTATION_REC\x12O\n\x1e\x63ommittee_publication_decision\x18\x07 \x01(\x0e\x32\'.chandra_bot_data_model.PUBLICATION_REC\x12\x31\n\x08\x61\x62stract\x18\x08 \x01(\x0b\x32\x1f.chandra_bot_data_model.Content\x12-\n\x04\x62ody\x18\t \x01(\x0b\x32\x1f.chandra_bot_data_model.Content\x12\x1b\n\x13mean_verified_score\x18\n \x01(\x02"6\n\x06\x41uthor\x12,\n\x05human\x18\x01 \x01(\x0b\x32\x1d.chandra_bot_data_model.Human"\xa0\x01\n\x08Reviewer\x12,\n\x05human\x18\x01 \x01(\x0b\x32\x1d.chandra_bot_data_model.Human\x12\x10\n\x08verified\x18\x02 \x01(\x08\x12\x1a\n\x12mean_present_score\x18\x03 \x01(\x02\x12\x1d\n\x15std_dev_present_score\x18\x04 \x01(\x02\x12\x19\n\x11number_of_reviews\x18\x05 \x01(\x05"\xae\x03\n\x06Review\x12\x32\n\x08reviewer\x18\x01 \x01(\x0b\x32 .chandra_bot_data_model.Reviewer\x12\x1a\n\x12presentation_score\x18\x02 \x01(\x02\x12 \n\x18normalized_present_score\x18\x03 \x01(\x02\x12=\n\x14\x63ommentary_to_author\x18\x04 \x01(\x0b\x32\x1f.chandra_bot_data_model.Content\x12<\n\x13\x63ommentary_to_chair\x18\x05 \x01(\x0b\x32\x1f.chandra_bot_data_model.Content\x12#\n\x1bpapers_written_with_authors\x18\x06 \x01(\x05\x12H\n\x16presentation_recommend\x18\x07 \x01(\x0e\x32(.chandra_bot_data_model.PRESENTATION_REC\x12\x46\n\x15publication_recommend\x18\x08 \x01(\x0e\x32\'.chandra_bot_data_model.PUBLICATION_REC"u\n\x07\x43ontent\x12,\n\x05human\x18\x01 \x01(\x0b\x32\x1d.chandra_bot_data_model.Human\x12\x17\n\x0fspelling_errors\x18\x02 \x01(\x05\x12\x15\n\rgrammar_score\x18\x03 \x01(\x02\x12\x0c\n\x04text\x18\x04 \x01(\t"9\n\tPaperBook\x12,\n\x05paper\x18\x01 \x03(\x0b\x32\x1d.chandra_bot_data_model.Paper*g\n\x10PRESENTATION_REC\x12\x1b\n\x17PRESENTATION_REC_REJECT\x10\x00\x12\x1b\n\x17PRESENTATION_REC_ACCEPT\x10\x01\x12\x19\n\x15PRESENTATION_REC_NONE\x10\x02*\x87\x01\n\x0fPUBLICATION_REC\x12\x1a\n\x16PUBLICATION_REC_REJECT\x10\x00\x12\x1a\n\x16PUBLICATION_REC_ACCEPT\x10\x01\x12"\n\x1ePUBLICATION_REC_ACCEPT_CORRECT\x10\x02\x12\x18\n\x14PUBLICATION_REC_NONE\x10\x03\x62\x06proto3',
)

_PRESENTATION_REC = _descriptor.EnumDescriptor(
    name="PRESENTATION_REC",
    full_name="chandra_bot_data_model.PRESENTATION_REC",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PRESENTATION_REC_REJECT",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRESENTATION_REC_ACCEPT",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRESENTATION_REC_NONE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1671,
    serialized_end=1774,
)
_sym_db.RegisterEnumDescriptor(_PRESENTATION_REC)

PRESENTATION_REC = enum_type_wrapper.EnumTypeWrapper(_PRESENTATION_REC)
_PUBLICATION_REC = _descriptor.EnumDescriptor(
    name="PUBLICATION_REC",
    full_name="chandra_bot_data_model.PUBLICATION_REC",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PUBLICATION_REC_REJECT",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PUBLICATION_REC_ACCEPT",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PUBLICATION_REC_ACCEPT_CORRECT",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PUBLICATION_REC_NONE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1777,
    serialized_end=1912,
)
_sym_db.RegisterEnumDescriptor(_PUBLICATION_REC)

PUBLICATION_REC = enum_type_wrapper.EnumTypeWrapper(_PUBLICATION_REC)
PRESENTATION_REC_REJECT = 0
PRESENTATION_REC_ACCEPT = 1
PRESENTATION_REC_NONE = 2
PUBLICATION_REC_REJECT = 0
PUBLICATION_REC_ACCEPT = 1
PUBLICATION_REC_ACCEPT_CORRECT = 2
PUBLICATION_REC_NONE = 3


_AFFILIATION = _descriptor.Descriptor(
    name="Affiliation",
    full_name="chandra_bot_data_model.Affiliation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="chandra_bot_data_model.Affiliation.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="aliases",
            full_name="chandra_bot_data_model.Affiliation.aliases",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=56,
    serialized_end=100,
)


_HUMAN = _descriptor.Descriptor(
    name="Human",
    full_name="chandra_bot_data_model.Human",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="chandra_bot_data_model.Human.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="aliases",
            full_name="chandra_bot_data_model.Human.aliases",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="hash_id",
            full_name="chandra_bot_data_model.Human.hash_id",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="current_affiliation",
            full_name="chandra_bot_data_model.Human.current_affiliation",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="previous_affiliation",
            full_name="chandra_bot_data_model.Human.previous_affiliation",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="last_degree_affiliation",
            full_name="chandra_bot_data_model.Human.last_degree_affiliation",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="orcid_url",
            full_name="chandra_bot_data_model.Human.orcid_url",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="orcid",
            full_name="chandra_bot_data_model.Human.orcid",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=103,
    serialized_end=395,
)


_PAPER = _descriptor.Descriptor(
    name="Paper",
    full_name="chandra_bot_data_model.Paper",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="number",
            full_name="chandra_bot_data_model.Paper.number",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="authors",
            full_name="chandra_bot_data_model.Paper.authors",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="reviews",
            full_name="chandra_bot_data_model.Paper.reviews",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="title",
            full_name="chandra_bot_data_model.Paper.title",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="year",
            full_name="chandra_bot_data_model.Paper.year",
            index=4,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="committee_presentation_decision",
            full_name="chandra_bot_data_model.Paper.committee_presentation_decision",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="committee_publication_decision",
            full_name="chandra_bot_data_model.Paper.committee_publication_decision",
            index=6,
            number=7,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="abstract",
            full_name="chandra_bot_data_model.Paper.abstract",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="body",
            full_name="chandra_bot_data_model.Paper.body",
            index=8,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="mean_verified_score",
            full_name="chandra_bot_data_model.Paper.mean_verified_score",
            index=9,
            number=10,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=398,
    serialized_end=839,
)


_AUTHOR = _descriptor.Descriptor(
    name="Author",
    full_name="chandra_bot_data_model.Author",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="human",
            full_name="chandra_bot_data_model.Author.human",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=841,
    serialized_end=895,
)


_REVIEWER = _descriptor.Descriptor(
    name="Reviewer",
    full_name="chandra_bot_data_model.Reviewer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="human",
            full_name="chandra_bot_data_model.Reviewer.human",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="verified",
            full_name="chandra_bot_data_model.Reviewer.verified",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="mean_present_score",
            full_name="chandra_bot_data_model.Reviewer.mean_present_score",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="std_dev_present_score",
            full_name="chandra_bot_data_model.Reviewer.std_dev_present_score",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="number_of_reviews",
            full_name="chandra_bot_data_model.Reviewer.number_of_reviews",
            index=4,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=898,
    serialized_end=1058,
)


_REVIEW = _descriptor.Descriptor(
    name="Review",
    full_name="chandra_bot_data_model.Review",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="reviewer",
            full_name="chandra_bot_data_model.Review.reviewer",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="presentation_score",
            full_name="chandra_bot_data_model.Review.presentation_score",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="normalized_present_score",
            full_name="chandra_bot_data_model.Review.normalized_present_score",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="commentary_to_author",
            full_name="chandra_bot_data_model.Review.commentary_to_author",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="commentary_to_chair",
            full_name="chandra_bot_data_model.Review.commentary_to_chair",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="papers_written_with_authors",
            full_name="chandra_bot_data_model.Review.papers_written_with_authors",
            index=5,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="presentation_recommend",
            full_name="chandra_bot_data_model.Review.presentation_recommend",
            index=6,
            number=7,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="publication_recommend",
            full_name="chandra_bot_data_model.Review.publication_recommend",
            index=7,
            number=8,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1061,
    serialized_end=1491,
)


_CONTENT = _descriptor.Descriptor(
    name="Content",
    full_name="chandra_bot_data_model.Content",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="human",
            full_name="chandra_bot_data_model.Content.human",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="spelling_errors",
            full_name="chandra_bot_data_model.Content.spelling_errors",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="grammar_score",
            full_name="chandra_bot_data_model.Content.grammar_score",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text",
            full_name="chandra_bot_data_model.Content.text",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1493,
    serialized_end=1610,
)


_PAPERBOOK = _descriptor.Descriptor(
    name="PaperBook",
    full_name="chandra_bot_data_model.PaperBook",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="paper",
            full_name="chandra_bot_data_model.PaperBook.paper",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1612,
    serialized_end=1669,
)

_HUMAN.fields_by_name["current_affiliation"].message_type = _AFFILIATION
_HUMAN.fields_by_name["previous_affiliation"].message_type = _AFFILIATION
_HUMAN.fields_by_name["last_degree_affiliation"].message_type = _AFFILIATION
_PAPER.fields_by_name["authors"].message_type = _AUTHOR
_PAPER.fields_by_name["reviews"].message_type = _REVIEW
_PAPER.fields_by_name["committee_presentation_decision"].enum_type = _PRESENTATION_REC
_PAPER.fields_by_name["committee_publication_decision"].enum_type = _PUBLICATION_REC
_PAPER.fields_by_name["abstract"].message_type = _CONTENT
_PAPER.fields_by_name["body"].message_type = _CONTENT
_AUTHOR.fields_by_name["human"].message_type = _HUMAN
_REVIEWER.fields_by_name["human"].message_type = _HUMAN
_REVIEW.fields_by_name["reviewer"].message_type = _REVIEWER
_REVIEW.fields_by_name["commentary_to_author"].message_type = _CONTENT
_REVIEW.fields_by_name["commentary_to_chair"].message_type = _CONTENT
_REVIEW.fields_by_name["presentation_recommend"].enum_type = _PRESENTATION_REC
_REVIEW.fields_by_name["publication_recommend"].enum_type = _PUBLICATION_REC
_CONTENT.fields_by_name["human"].message_type = _HUMAN
_PAPERBOOK.fields_by_name["paper"].message_type = _PAPER
DESCRIPTOR.message_types_by_name["Affiliation"] = _AFFILIATION
DESCRIPTOR.message_types_by_name["Human"] = _HUMAN
DESCRIPTOR.message_types_by_name["Paper"] = _PAPER
DESCRIPTOR.message_types_by_name["Author"] = _AUTHOR
DESCRIPTOR.message_types_by_name["Reviewer"] = _REVIEWER
DESCRIPTOR.message_types_by_name["Review"] = _REVIEW
DESCRIPTOR.message_types_by_name["Content"] = _CONTENT
DESCRIPTOR.message_types_by_name["PaperBook"] = _PAPERBOOK
DESCRIPTOR.enum_types_by_name["PRESENTATION_REC"] = _PRESENTATION_REC
DESCRIPTOR.enum_types_by_name["PUBLICATION_REC"] = _PUBLICATION_REC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Affiliation = _reflection.GeneratedProtocolMessageType(
    "Affiliation",
    (_message.Message,),
    {
        "DESCRIPTOR": _AFFILIATION,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.Affiliation)
    },
)
_sym_db.RegisterMessage(Affiliation)

Human = _reflection.GeneratedProtocolMessageType(
    "Human",
    (_message.Message,),
    {
        "DESCRIPTOR": _HUMAN,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.Human)
    },
)
_sym_db.RegisterMessage(Human)

Paper = _reflection.GeneratedProtocolMessageType(
    "Paper",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAPER,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.Paper)
    },
)
_sym_db.RegisterMessage(Paper)

Author = _reflection.GeneratedProtocolMessageType(
    "Author",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHOR,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.Author)
    },
)
_sym_db.RegisterMessage(Author)

Reviewer = _reflection.GeneratedProtocolMessageType(
    "Reviewer",
    (_message.Message,),
    {
        "DESCRIPTOR": _REVIEWER,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.Reviewer)
    },
)
_sym_db.RegisterMessage(Reviewer)

Review = _reflection.GeneratedProtocolMessageType(
    "Review",
    (_message.Message,),
    {
        "DESCRIPTOR": _REVIEW,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.Review)
    },
)
_sym_db.RegisterMessage(Review)

Content = _reflection.GeneratedProtocolMessageType(
    "Content",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTENT,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.Content)
    },
)
_sym_db.RegisterMessage(Content)

PaperBook = _reflection.GeneratedProtocolMessageType(
    "PaperBook",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAPERBOOK,
        "__module__": "chandra_bot_data_model_pb2"
        # @@protoc_insertion_point(class_scope:chandra_bot_data_model.PaperBook)
    },
)
_sym_db.RegisterMessage(PaperBook)


# @@protoc_insertion_point(module_scope)
