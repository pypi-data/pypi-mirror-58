""" Module responsible for hosting all EVC imported from backend
or from YAML file. Any operation performed by evc_manager over an EVC
has to pass through this module to guarantee we have the right EVC. """


from .cli import CliOptions
from .evc_to_dict import convert_class
from ..outputs.to_table import filter_per_nni


class EvcsList(object):
    """ List of EVCs """

    def __init__(self, evc_list=None):
        """ Init method """
        self._evcs = list()
        if evc_list:
            self.evcs = evc_list

    @property
    def evcs(self):
        """ Getter """
        return self._evcs

    @evcs.setter
    def evcs(self, evc_list):
        """ Setter """
        # TODO: Validate input
        self._evcs = self.filter(evc_list)

    def to_dict(self):
        """ Convert to self to dictionary """
        return convert_class(self.evcs)

    def find(self, target_evc):
        """ Return True if a specific EVC already exists """
        for evc in self.evcs:
            if target_evc == evc:
                return evc
        return False

    @staticmethod
    def has_device(evc_list):
        """ Used to check if an UNI filter provided has any device on it
        Args:
            evc_list: list of evcs
        Return:
            list of EVCs (original or filtered by device)
        """
        if CliOptions().has_uni_device:
            evcs_to_add = list()
            for evc in evc_list:
                for uni in evc.unis:
                    if uni.device == CliOptions().has_uni_device:
                        evcs_to_add.append(evc)
                        break

            return evcs_to_add
        else:
            return evc_list

    @staticmethod
    def has_interface(evc_list):
        """ Used to check if an UNI filter provided has any interface on it
        Args:
            evc_list: list of evcs
        Return:
            list of EVCs (original or filtered by interface)
        """
        if CliOptions().has_uni_interface:
            evcs_to_add = list()
            for evc in evc_list:
                for uni in evc.unis:
                    if uni.interface_name == CliOptions().has_uni_interface:
                        evcs_to_add.append(evc)
                        break

            return evcs_to_add
        else:
            return evc_list

    @staticmethod
    def has_tag_value(evc_list):
        """ Used to check if an UNI filter provided has any tag value on it
        Args:
            evc_list: list of evcs
        Return:
            list of EVCs (original or filtered by tag value)
        """
        if CliOptions().has_uni_tag_value:
            evcs_to_add = list()
            for evc in evc_list:
                for uni in evc.unis:
                    if uni.tag.value == CliOptions().has_uni_tag_value:
                        evcs_to_add.append(evc)
                        break

            return evcs_to_add
        else:
            return evc_list

    def has_nni_name_primary(self, nni_name, evc_list):
        """ Return list of EVCs with nni_name on the primary path
        Args:
            nni_name: NNI's name
            evc_list: List of EVCs
        Return:
            list of EVCs
        """

    @staticmethod
    def evc_list_after_nni_filter(nni_name, nni_type, evc_list):
        """ Create the final list of EVCs after filtering per NNI
        Args:
            nni_name: NNI Name
            nni_type: type of NNI (any, primary, backup)
            evc_list: list of EVCs
        Returns:
            list of evcs
        """
        evcs_to_add = list()
        for evc in evc_list:
            if filter_per_nni(evc, target_nni=nni_name, filter_per_type=nni_type):
                evcs_to_add.append(evc)
        return evcs_to_add

    def has_nni_filters(self, evc_list):
        """ Used to filter per NNI's name. NNI could be part of the primary, backup,
        or both paths.
        Args:
            evc_list: list of evcs
        Return:
            list of EVCs (original or filtered by NNI)
        """
        if not CliOptions().has_nni_filters:
            return evc_list

        if CliOptions().has_nni_name:
            # It doesn't matter if it is primary or backup
            return self.evc_list_after_nni_filter(CliOptions().has_nni_name,
                                                  "any", evc_list)
        else:
            if CliOptions().has_nni_name_primary:
                evc_list = self.evc_list_after_nni_filter(CliOptions().has_nni_name_primary,
                                                          "primary", evc_list)

            if CliOptions().has_nni_name_backup:
                return self.evc_list_after_nni_filter(CliOptions().has_nni_name_backup,
                                                      "backup", evc_list)
            return evc_list

    def filter(self, evc_list):
        """ Apply filters if any. """
        if not CliOptions().has_uni_filters and not CliOptions().has_nni_filters:
            return evc_list

        evcs = self.has_tag_value(self.has_interface(self.has_device(evc_list)))
        return self.has_nni_filters(evcs)
