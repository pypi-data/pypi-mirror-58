// @flow
import type { DeckSlotId } from '@opentrons/shared-data'
import type {
  ProtocolFile as V3ProtocolFile,
  _AspDispAirgapParams,
  BlowoutParams,
  TouchTipParams,
  PipetteAccessParams,
  MoveToSlotParams,
  DelayParams,
} from './schemaV3'
export type { BlowoutParams, FilePipette, FileLabware } from './schemaV4'

export type FileModule = {|
  slot: DeckSlotId,
  moduleType: string, // see spec for enum
  model: string,
|}

export type EngageMagnetParams = {|
  module: string,
  engageHeight: number,
|}

export type DisengageMagnetParams = {|
  module: string,
|}

export type Command =
  | {|
      command: 'aspirate' | 'dispense' | 'airGap',
      params: _AspDispAirgapParams,
    |}
  | {|
      command: 'blowout',
      params: BlowoutParams,
    |}
  | {|
      command: 'touchTip',
      params: TouchTipParams,
    |}
  | {|
      command: 'pickUpTip' | 'dropTip',
      params: PipetteAccessParams,
    |}
  | {|
      command: 'moveToSlot',
      params: MoveToSlotParams,
    |}
  | {|
      command: 'delay',
      params: DelayParams,
    |}
  | {| command: 'magneticModule/engageMagnet', params: EngageMagnetParams |}
  | {|
      command: 'magneticModule/disengageMagnet',
      params: DisengageMagnetParams,
    |}

// NOTE: must be kept in sync with '../schemas/4.json'
export type ProtocolFile<DesignerApplicationData> = {|
  ...V3ProtocolFile<DesignerApplicationData>,
  schemaVersion: 4,
  // TODO: Ian 2019-11-11 make modules a required key when v4 is legit
  modules?: {
    [moduleId: string]: FileModule,
  },
  commands: Array<Command>,
|}
