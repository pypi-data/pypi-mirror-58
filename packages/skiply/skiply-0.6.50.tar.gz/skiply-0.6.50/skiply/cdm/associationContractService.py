#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class AssociationContractService(SkiplyBase):
    ''' Device '''
    __tablename__ = 'contract_service'
    
    contract_id = Column('contract_id', Integer, ForeignKey("so_contract.id"), nullable=False, primary_key=True)
    service_id = Column('service_id', Integer, ForeignKey("so_service.id"), nullable=False, primary_key=True)

    contract = relationship("Contract", back_populates="services")
    service = relationship("Service", back_populates="contracts")

    def __init__(self, contract_id, service_id):
        self.contract_id = contract_id
        self.service_id = service_id

    def __repr__(self):
        return '<Association Contract %r / Service %r>' % (self.contract_id, self.service_id)

def get_contracts_for_services(service_ids):
	session = db_session()
	try:
        results = session.query(AssociationContractService).filter(AssociationContractService.service_id._in(service_ids)).all()
    except Exception as e:
    	print("DB Request get_contracts_for_services(service_ids) Failed with error : {}".format(e))
    	results = None
    finally:
    	session.close()

    return results